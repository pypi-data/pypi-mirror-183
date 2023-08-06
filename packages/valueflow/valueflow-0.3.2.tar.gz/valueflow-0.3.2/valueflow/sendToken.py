from web3 import Web3
from . import Valueflow
from .conf.ABI import DISPERSE_ABI
from .conf.contract_address import DISPERSE_CONTRACT_ADDRESS
from .exception import PayableError, GasPayableError


class SendToken(Valueflow):

    async def send_token(self, send_amount: int, to_address: str, from_address: str, from_address_pri_key: str,
                         eip1559: bool = False):
        """
        发送主网代币
        :param send_amount: 发送代币数量
        :param to_address: 接受地址
        :param from_address: 发送地址的公钥
        :param from_address_pri_key: 发送地址的私钥
        :param eip1559: 是否按eip1559发送交易
        """
        gas = 21000
        balance = self.w3.eth.get_balance(from_address)
        gas_price = self.w3.eth.gas_price
        if send_amount == 0:
            send_amount = balance - gas * gas_price
            if send_amount > 0:
                await self.send_transaction(send_amount, to_address, from_address, from_address_pri_key, gas,
                                            self.w3.fromWei(gas_price, 'gwei'))
            else:
                raise PayableError(f"{from_address} 账号余额不足")
        else:
            balance = balance - send_amount - (gas * gas_price)
            if balance > 0:
                await self.send_transaction_eip1559(send_amount, to_address, from_address, from_address_pri_key, gas) \
                    if eip1559 \
                    else await self.send_transaction(send_amount, to_address, from_address, from_address_pri_key, gas)
            else:
                raise PayableError(f"{from_address} 账号余额不足")

    async def send_contract_token(self, send_amount: float, to_address: str, from_address: str,
                                  from_address_pri_key: str,
                                  smart_contract_address: str,
                                  abi: list, eip1559: bool = False):
        """
        发送ERC20智能合约代币
        :param send_amount: 发送代币数量
        :param to_address: 接收地址
        :param from_address: 发送地址的公钥
        :param from_address_pri_key: 发送地址的私钥
        :param smart_contract_address: 智能合约地址
        :param abi: 智能合约abi
        :param eip1559: 是否按eip1559发送交易
        """
        gas = 80000
        contract_address = Web3.toChecksumAddress(smart_contract_address)
        contract = self.w3.eth.contract(address=contract_address, abi=abi)
        send_amount = self.convert_contract_token_to_min_uint(contract, send_amount)
        balance = self.w3.eth.get_balance(from_address)
        contract_balance = contract.functions.balanceOf(from_address).call()
        if contract_balance > 0 and balance > 0:
            gas_price = self.w3.eth.gas_price
            gas_payable = balance - (gas * gas_price)
            if gas_payable >= 0:
                if send_amount == 0:
                    await self.send_contract_transaction_eip1559(contract, contract_balance, to_address, from_address,
                                                                 from_address_pri_key, gas) \
                        if eip1559 else \
                        await self.send_contract_transaction(contract, contract_balance, to_address, from_address,
                                                             from_address_pri_key, gas,
                                                             self.w3.fromWei(gas_price, 'gwei'))
                else:
                    if contract_balance - send_amount >= 0:
                        await self.send_contract_transaction_eip1559(contract, send_amount, to_address,
                                                                     from_address,
                                                                     from_address_pri_key, gas) \
                            if eip1559 else \
                            await self.send_contract_transaction(contract, send_amount, to_address,
                                                                 from_address,
                                                                 from_address_pri_key, gas,
                                                                 self.w3.fromWei(gas_price, 'gwei'))
            else:
                raise GasPayableError(f"{from_address} 账号余额不足支付gas")

    async def disperse_token(self, from_address_pub_key: str, from_address_pri_key: str, recipients: list,
                             values: list, total_send_amount: int, eip1559: bool = False):
        to_address = DISPERSE_CONTRACT_ADDRESS[self.chain_id]
        recipients = [self.w3.toChecksumAddress(i) for i in recipients]
        disperse_contract = self.w3.eth.contract(address=to_address, abi=DISPERSE_ABI)
        tx_data = disperse_contract.encodeABI(fn_name="disperseEther", args=[recipients, values])
        gas = self.w3.eth.estimateGas(
            {'from': from_address_pub_key, 'to': to_address, 'data': tx_data, 'value': total_send_amount}) * 1.8
        gas = int(gas)
        await self.send_tx_contract_transaction_eip1559(from_address_pub_key=from_address_pub_key,
                                                        from_address_pri_key=from_address_pri_key,
                                                        smart_contract_address=to_address,
                                                        tx_data=tx_data, send_amount=total_send_amount, gas=gas) \
            if eip1559 else \
            await self.send_tx_contract_transaction(from_address_pub_key=from_address_pub_key,
                                                    from_address_pri_key=from_address_pri_key,
                                                    smart_contract_address=to_address,
                                                    tx_data=tx_data, send_amount=total_send_amount, gas=gas)

    async def disperse_contract_token(self, token_address: str, from_address_pub_key: str, from_address_pri_key: str,
                                      recipients: list, values: list, eip1559: bool = False):
        to_address = DISPERSE_CONTRACT_ADDRESS[self.chain_id]
        recipients = [self.w3.toChecksumAddress(i) for i in recipients]
        token_address = self.w3.toChecksumAddress(token_address)
        disperse_contract = self.w3.eth.contract(address=to_address, abi=DISPERSE_ABI)
        tx_data = disperse_contract.encodeABI(fn_name="disperseToken", args=[token_address, recipients, values])
        gas = self.w3.eth.estimateGas(
            {'from': from_address_pub_key, 'to': to_address, 'data': tx_data}) * 1.8
        gas = int(gas)
        await self.send_tx_contract_transaction_eip1559(from_address_pub_key=from_address_pub_key,
                                                        from_address_pri_key=from_address_pri_key,
                                                        smart_contract_address=to_address,
                                                        tx_data=tx_data,
                                                        gas=gas) \
            if eip1559 else \
            await self.send_tx_contract_transaction(
                from_address_pub_key=from_address_pub_key,
                from_address_pri_key=from_address_pri_key,
                smart_contract_address=to_address,
                tx_data=tx_data, gas=gas)
