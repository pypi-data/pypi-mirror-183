from eth_account.datastructures import SignedTransaction
from web3 import Web3
from web3.contract import Contract
from web3.middleware import geth_poa_middleware
from eth_account.messages import encode_defunct
from abc import ABCMeta
import asyncio
from web3.exceptions import (
    TransactionNotFound,
)

from conf.ABI import ERC20_ABI
from conf.evm_network_config import EVM_NETWORK
from src.accountManager import get_account, write_yaml
from .exception import TransactionError, TransactionTimeoutError


class Valueflow(metaclass=ABCMeta):
    def __init__(self, network: str = 'goerli', rpc_url: str = None):
        """
        :param network: 使用的主网
        目前支持的主网：ethereum/polygon/fantom/binance-smart-chain/xdai
        """
        if rpc_url:
            self.w3 = Web3(Web3.HTTPProvider(rpc_url))
            self.chain_id = self.w3.eth.chain_id
        else:
            self.w3 = Web3(Web3.HTTPProvider(EVM_NETWORK[network]['rpcUrl']))
            self.chain_id = EVM_NETWORK[network]['chainId']
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    def message_signature(self, pri_key: str, message: str) -> str:
        """
        离线消息签名
        :param message: 待签名信息
        :param pri_key: 私钥
        :return: 离线消息签名
        """
        message = encode_defunct(text=message)
        signature = self.w3.eth.account.sign_message(message, private_key=pri_key)
        signature = self.w3.toHex(signature.signature)
        return signature

    def is_allowance(self, owner: str, spender: str, contract_address: str, allowance_amount: int = None) -> bool:
        """
        检查合约账户是否授权
        :param owner: 账户
        :param spender: 消费者
        :param contract_address: 合约地址
        :param allowance_amount: 授权金额
        :return: true or false
        """
        owner = self.w3.toChecksumAddress(owner)
        spender = self.w3.toChecksumAddress(spender)
        contract_address = self.w3.toChecksumAddress(contract_address)
        contract = self.w3.eth.contract(address=contract_address, abi=ERC20_ABI)
        res = contract.functions.allowance(owner, spender).call()
        if allowance_amount:
            if res - allowance_amount >= 0:
                return True
            else:
                return False
        else:
            if res > 0:
                return True
            else:
                return False

    def check_token_balance(self, token_address: str, from_address: str, convert_to_max_uint: bool = False) -> float:
        contract_address = Web3.toChecksumAddress(token_address)
        contract = self.w3.eth.contract(address=contract_address, abi=ERC20_ABI)
        contract_balance = contract.functions.balanceOf(from_address).call()
        if convert_to_max_uint:
            return self.convert_contract_token_to_max_uint(contract, contract_balance)
        return contract_balance

    def filter_account(self, filename: str):
        """
        过滤掉账户余额为零的账户，并生成新的账号名单
        :param filename: 文件名
        """
        if '.yml' not in filename:
            filename = f'{filename}.yml'
        accounts = get_account(filename)
        account_dict = {}
        for pub, pri in accounts.items():
            if self.w3.eth.get_balance(pub) > 0:
                account_dict[pub] = pri
        if account_dict:
            new_file_name = 'filter_' + filename
            write_yaml(new_file_name, account_dict)

    @staticmethod
    def convert_contract_token_to_max_uint(contract: Contract, contract_balance: int) -> float:
        """
        智能合约账户代币单位转换成最大单位
        :param contract: 智能合约ABI
        :param contract_balance: 智能合约代币余额
        :return: 转换单位后的合约余额
        """
        contract_decimals = contract.functions.decimals().call()
        decimals = 10 ** contract_decimals
        contract_balance = contract_balance / decimals
        return contract_balance

    @staticmethod
    def convert_contract_token_to_min_uint(contract: Contract, contract_balance: float) -> int:
        """
        智能合约账户代币单位转换成最小单位
        :param contract: 智能合约ABI
        :param contract_balance: 智能合约代币余额
        :return: 转换单位后的合约余额
        """
        contract_decimals = contract.functions.decimals().call()
        decimals = 10 ** contract_decimals
        contract_balance = contract_balance * decimals
        return contract_balance

    async def send_transaction(self, send_amount: int, to_address: str, from_address_pub_key: str,
                               from_address_pri_key: str, gas: int, gas_price: [int, float] = 0):
        """
        发送账户交易
        :param from_address_pub_key: 发送地址的公钥
        :param from_address_pri_key: 发送地址的私钥
        :param send_amount: 发送余额
        :param to_address: 接受地址
        :param gas: gas值
        :param gas_price: gas价格
        """
        nonce = self.w3.eth.get_transaction_count(from_address_pub_key)
        transaction = {
            'nonce': nonce,
            'chainId': self.chain_id,
            'to': to_address,
            'value': send_amount,
            'gas': gas,
            'gasPrice': self.w3.toWei(gas_price, 'gwei') if gas_price else self.w3.eth.gas_price,
        }
        signed_txn = self.w3.eth.account.sign_transaction(transaction, from_address_pri_key)
        await self.process_transaction(signed_txn, from_address_pub_key, to_address)

    async def send_transaction_eip1559(self, send_amount: int, to_address: str, from_address_pub_key: str,
                                       from_address_pri_key: str, gas: int,
                                       max_priority_fee_per_gas: [int, float] = 0,
                                       max_fee_per_gas: [int, float] = 0):
        """
        发送账户交易
        :param from_address_pub_key: 发送地址的公钥
        :param from_address_pri_key: 发送地址的私钥
        :param send_amount: 发送余额
        :param to_address: 接受地址
        :param gas: gas值
        :param max_priority_fee_per_gas: 矿工费
        :param max_fee_per_gas: 支付的最大费用
        """
        nonce = self.w3.eth.get_transaction_count(from_address_pub_key)
        max_priority_fee_per_gas = self.w3.toWei(max_priority_fee_per_gas, 'gwei') if max_priority_fee_per_gas \
            else self.w3.eth.max_priority_fee
        max_fee_per_gas = self.w3.toWei(max_fee_per_gas, 'gwei') if max_fee_per_gas \
            else int(1.5 * self.w3.eth.gas_price)
        transaction = {
            'nonce': nonce,
            'chainId': self.chain_id,
            'to': to_address,
            'value': send_amount,
            'gas': gas,
            'maxPriorityFeePerGas': max_priority_fee_per_gas,
            'maxFeePerGas': max_fee_per_gas
        }
        signed_txn = self.w3.eth.account.sign_transaction(transaction, from_address_pri_key)
        await self.process_transaction(signed_txn, from_address_pub_key, to_address)

    async def send_contract_transaction(self, contract: Contract, send_amount: int, to_address: str,
                                        from_address_pub_key: str,
                                        from_address_pri_key: str, gas: int,
                                        gas_price: [int, float] = 0):
        """
        发送智能合约账户交易(必须是ERC20合约）
        :param contract: 构建好的智能合约
        :param send_amount: 发送余额
        :param to_address: 接受地址
        :param from_address_pub_key: 发送地址的公钥
        :param from_address_pri_key: 发送地址的私钥
        :param gas: gas值
        :param gas_price: 当前gas价格（单位： gwei）
        """
        nonce = self.w3.eth.get_transaction_count(from_address_pub_key)
        gas_price = self.w3.toWei(gas_price, 'gwei') if gas_price else self.w3.eth.gas_price
        contract_txn = contract.functions.transfer(
            to_address,
            send_amount,
        ).buildTransaction({
            'nonce': nonce,
            'chainId': self.chain_id,
            'gas': gas,
            'gasPrice': gas_price
        })
        signed_txn = self.w3.eth.account.sign_transaction(contract_txn, private_key=from_address_pri_key)
        await self.process_transaction(signed_txn, from_address_pub_key, to_address)

    async def send_contract_transaction_eip1559(self, contract: Contract, send_amount: int, to_address: str,
                                                from_address_pub_key: str,
                                                from_address_pri_key: str, gas: int,
                                                max_priority_fee_per_gas: [int, float] = 0,
                                                max_fee_per_gas: [int, float] = 0):
        """
        发送智能合约账户交易(必须是ERC20合约）
        :param contract: 构建好的智能合约
        :param send_amount: 发送余额
        :param to_address: 接受地址
        :param from_address_pub_key: 发送地址的公钥
        :param from_address_pri_key: 发送地址的私钥
        :param gas: gas值
        :param max_priority_fee_per_gas: 矿工费
        :param max_fee_per_gas: 支付的最大费用
        """
        nonce = self.w3.eth.get_transaction_count(from_address_pub_key)
        max_priority_fee_per_gas = self.w3.toWei(max_priority_fee_per_gas, 'gwei') if max_priority_fee_per_gas \
            else self.w3.eth.max_priority_fee
        max_fee_per_gas = self.w3.toWei(max_fee_per_gas, 'gwei') if max_fee_per_gas \
            else int(1.5 * self.w3.eth.gas_price)
        contract_txn = contract.functions.transfer(
            to_address,
            send_amount,
        ).buildTransaction({
            'nonce': nonce,
            'chainId': self.chain_id,
            'gas': gas,
            'maxPriorityFeePerGas': max_priority_fee_per_gas,
            'maxFeePerGas': max_fee_per_gas
        })
        signed_txn = self.w3.eth.account.sign_transaction(contract_txn, private_key=from_address_pri_key)
        await self.process_transaction(signed_txn, from_address_pub_key, to_address)

    async def send_tx_contract_transaction(self, from_address_pub_key: str, from_address_pri_key: str,
                                           smart_contract_address: str,
                                           tx_data: str, send_amount: int = 0,
                                           gas: int = 210000,
                                           gas_price: [int, float] = 0):
        """
        根据构建成的data发送合约交易
        :param from_address_pub_key: 发送地址的公钥
        :param from_address_pri_key: 发送地址的私钥
        :param smart_contract_address: 接受地址
        :param tx_data: Input Data
        :param send_amount: 发送余额（即 msg.value 默认为 0）
        :param gas: gas值 (默认为 210000)
        :param gas_price: 当前gas价格（单位： gwei）
        """
        nonce = self.w3.eth.get_transaction_count(from_address_pub_key)
        gas_price = self.w3.toWei(gas_price, 'gwei') if gas_price else self.w3.eth.gas_price
        to_address = Web3.toChecksumAddress(smart_contract_address)
        from_address_pub_key = Web3.toChecksumAddress(from_address_pub_key)
        tx = {
            'chainId': self.chain_id,
            'nonce': nonce,
            'to': to_address,
            'value': send_amount,
            'gas': gas,
            'gasPrice': gas_price,
            'data': f'{tx_data}'
        }
        sign_tx = self.w3.eth.account.sign_transaction(tx, from_address_pri_key)
        await self.process_transaction(sign_tx, from_address_pub_key, to_address)

    async def send_tx_contract_transaction_eip1559(self, from_address_pub_key: str,
                                                   from_address_pri_key: str,
                                                   smart_contract_address: str,
                                                   tx_data: str, send_amount: int = 0,
                                                   gas: int = 210000,
                                                   max_priority_fee_per_gas: [int, float] = 0,
                                                   max_fee_per_gas: [int, float] = 0,
                                                   ):
        """
        根据构建成的data发送合约交易
        :param from_address_pub_key: 发送地址的公钥
        :param from_address_pri_key: 发送地址的私钥
        :param smart_contract_address: 接受地址
        :param tx_data: Input Data
        :param send_amount: 发送余额（即 msg.value 默认为 0）
        :param gas: gas值 (默认为 210000)
        :param max_priority_fee_per_gas: 矿工费
        :param max_fee_per_gas: 支付的最大费用
        """
        nonce = self.w3.eth.get_transaction_count(from_address_pub_key)
        max_priority_fee_per_gas = self.w3.toWei(max_priority_fee_per_gas, 'gwei') if max_priority_fee_per_gas \
            else self.w3.eth.max_priority_fee
        max_fee_per_gas = self.w3.toWei(max_fee_per_gas, 'gwei') if max_fee_per_gas \
            else int(1.5 * self.w3.eth.gas_price)
        to_address = Web3.toChecksumAddress(smart_contract_address)
        from_address_pub_key = Web3.toChecksumAddress(from_address_pub_key)
        tx = {
            'chainId': self.chain_id,
            'nonce': nonce,
            'to': to_address,
            'value': send_amount,
            'gas': gas,
            'maxPriorityFeePerGas': max_priority_fee_per_gas,
            'maxFeePerGas': max_fee_per_gas,
            'data': f'{tx_data}'
        }
        sign_tx = self.w3.eth.account.sign_transaction(tx, from_address_pri_key)
        await self.process_transaction(sign_tx, from_address_pub_key, to_address)

    async def process_transaction(self, signed_txn: SignedTransaction, from_address: str, to_address: str):
        """
        异步处理交易过程，判断交易状态
        :param signed_txn: tx
        :param from_address: 发送地址
        :param to_address: 接受地址
        """
        try:
            transaction_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            transaction_hash = self.w3.toHex(transaction_hash)
        except ValueError:
            raise ValueError(f"账号: {from_address} 发送的该笔交易无法执行")
        else:
            # 同步捕获交易
            # self.w3.eth.wait_for_transaction_receipt(transaction_hash=transaction_hash, poll_latency=1)
            count_time = 0
            while 1:
                try:
                    txn_receipt = self.w3.eth.getTransactionReceipt(transaction_hash)
                except TransactionNotFound:
                    txn_receipt = None
                if txn_receipt is not None and txn_receipt['blockHash'] is not None and txn_receipt['status'] is not None:
                    break
                await asyncio.sleep(2)
                count_time += 2
                if count_time == 180:
                    break
            if txn_receipt.status == 1:
                print(f"from:{from_address} to:{to_address} 交易发送成功")
            else:
                print(f"from:{from_address} to:{to_address} 交易发送失败")
                if count_time == 180:
                    raise TransactionTimeoutError(f"账号:{from_address} 发出的交易超时")
                else:
                    raise TransactionError(f"from:{from_address} to:{to_address} 交易发送失败")
