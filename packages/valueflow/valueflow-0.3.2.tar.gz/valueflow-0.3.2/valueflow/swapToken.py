import time
from web3.types import TxReceipt
from web3.contract import Contract
from src.valueflow import DefiTools
from src.params import UNISWAP_ROUTER_ABI


def process(func):
    def wrapper(self, from_address: str, from_address_pri_key: str, smart_contract_address: str,
                token_address_path: list, amount: int, slippage: float = 0.001):
        """
        :param self: __dict__
        :param from_address: 发送地址公钥
        :param from_address_pri_key: 发送地址私钥
        :param smart_contract_address: 路由合约地址
        :param token_address_path: 代币交换路径 address[]
        :param amount: 余额
        :param slippage: 滑点
        """
        from_address = self.w3.toChecksumAddress(from_address)
        smart_contract_address = self.w3.toChecksumAddress(smart_contract_address)
        sell_token_address = self.w3.toChecksumAddress(token_address_path[0])
        buy_token_address = self.w3.toChecksumAddress(token_address_path[1])
        token_address_path = [sell_token_address, buy_token_address]
        contract = self.w3.eth.contract(address=smart_contract_address, abi=UNISWAP_ROUTER_ABI)
        nonce = self.w3.eth.getTransactionCount(from_address)
        return func(self, smart_contract_address, contract, nonce, from_address, from_address_pri_key, amount,
                    token_address_path, slippage)

    return wrapper


class SwapToken(DefiTools):
    """
    代币交互，授权仅限于ECR20合约代币。交易仅限于uniswap v2类合约
    交易代币一定要注意交易池
    """

    async def approve(self, from_address: str, from_address_pri_key: str, approve_token_address: str,
                      approve_token_ABI: list, gas: int = 210000, is_approve: int = 1) -> TxReceipt:
        """
        代币授权
        :param from_address: 发送地址的公钥
        :param from_address_pri_key: 发送地址的私钥
        :param approve_token_address: 需要授权的合约地址
        :param approve_token_ABI: 授权合约ABI
        :param gas: gas值, 默认为 210000
        :param is_approve: 是否授权，如果想取消授权，输入为 0 即可
        :return: TxReceipt 用于交易结果判断
        """
        approve_amount = 2 ** 256 - 1 if is_approve else 0
        approve_token_address = self.w3.toChecksumAddress(approve_token_address)
        from_address = self.w3.toChecksumAddress(from_address)
        token_contract = self.w3.eth.contract(address=approve_token_address, abi=approve_token_ABI)
        nonce = self.w3.eth.getTransactionCount(from_address)
        tx = token_contract.functions.approve(approve_token_address, approve_amount).buildTransaction({
            'chainId': self.chain_id,
            'gas': gas,
            'gasPrice': self.get_gas_price(self.network),
            'nonce': nonce,
        })
        signed_txn = self.w3.eth.account.sign_transaction(tx, private_key=from_address_pri_key)
        await self.process_transaction(signed_txn, from_address, approve_token_address)

        transaction_hash = self.w3.eth.account.sign_transaction(tx, from_address_pri_key)
        return self.w3.eth.wait_for_transaction_receipt(transaction_hash=transaction_hash, poll_latency=1)

    def get_amount(self, smart_contract_address: str, amount: int, token_a_address: str, token_b_address: str):
        contract = self.w3.eth.contract(address=smart_contract_address, abi=UNISWAP_ROUTER_ABI)
        token_a = self.w3.toChecksumAddress(token_a_address)
        token_b = self.w3.toChecksumAddress(token_b_address)
        address_list = token_a, token_b
        amount_in = contract.functions.getAmountsIn(amount, address_list).call()
        amount_out = contract.functions.getAmountsOut(amount, address_list).call()
        return amount_in, amount_out

    @process
    async def swap_exact_eth_for_token(self, smart_contract_address: str, contract: Contract,
                                       nonce: int, from_address: str, from_address_pri_key: str,
                                       amount: int, token_address_path: list, slippage: float = 0.001,
                                       gas: int = 210000):
        """
        用精确的ETH数量交换得到对应的token(数量不固定）
        """
        amount_out = contract.functions.getAmountsOut(amount, token_address_path).call()[1]
        amount_out = int(amount_out * (1 - slippage))
        tx = contract.functions.swapExactETHForTokens(
            amount_out,
            [token_address_path[0], token_address_path[1]],
            from_address,
            int(time.time()) + 1000000).buildTransaction({
                'chainId': self.chain_id,
                'gas': gas,
                'gasPrice': self.get_gas_price(self.network),
                'nonce': nonce,
        })
        await self.send_tx_contract_transaction(nonce=nonce, from_address_pub_key=from_address,
                                                from_address_pri_key=from_address_pri_key,
                                                smart_contract_address=smart_contract_address,
                                                tx_data=tx['data'], send_amount=amount)

    @process
    async def swap_eth_for_exact_token(self, smart_contract_address: str, contract: Contract,
                                       nonce: int, from_address: str, from_address_pri_key: str,
                                       amount: int, token_address_path: list, slippage: float = 0.001,
                                       gas: int = 210000):
        """
        用(数量不固定）的ETH数量交换得到对应精确数量的token
        """
        amount_in = contract.functions.getAmountsIn(amount, token_address_path).call()[0]
        amount_in = int(amount_in * (1 + slippage))
        tx = contract.functions.swapETHForExactTokens(
            amount,
            [token_address_path[0], token_address_path[1]],
            from_address,
            int(time.time()) + 1000000).buildTransaction({
                'chainId': self.chain_id,
                'gas': gas,
                'gasPrice': self.get_gas_price(self.network),
                'nonce': nonce,
        })
        await self.send_tx_contract_transaction(nonce=nonce, from_address_pub_key=from_address,
                                                from_address_pri_key=from_address_pri_key,
                                                smart_contract_address=smart_contract_address,
                                                tx_data=tx['data'], send_amount=amount_in)

    @process
    async def swap_exact_token_for_eth(self, smart_contract_address: str, contract: Contract,
                                       nonce: int, from_address: str, from_address_pri_key: str,
                                       amount: int, token_address_path: list, slippage: float = 0.001,
                                       gas: int = 210000):
        """
        用精确的ETH数量交换得到对应的token(数量不固定）
        """
        amount_out = contract.functions.getAmountsOut(amount, token_address_path).call()[1]
        amount_out = int(amount_out * (1 - slippage))
        tx = contract.functions.swapExactTokensForETH(
            amount, amount_out,
            [token_address_path[0], token_address_path[1]],
            from_address,
            int(time.time()) + 1000000).buildTransaction({
                'chainId': self.chain_id,
                'gas': gas,
                'gasPrice': self.get_gas_price(self.network),
                'nonce': nonce,
        })
        await self.send_tx_contract_transaction(nonce=nonce, from_address_pub_key=from_address,
                                                from_address_pri_key=from_address_pri_key,
                                                smart_contract_address=smart_contract_address,
                                                tx_data=tx['data'])

    @process
    async def swap_token_for_exact_eth(self, smart_contract_address: str, contract: Contract,
                                       nonce: int, from_address: str, from_address_pri_key: str,
                                       amount: int, token_address_path: list, slippage: float = 0.001,
                                       gas: int = 210000):
        """
        用(数量不固定）的Token交换得到对应精确数量的ETH
        """
        amount_in = contract.functions.getAmountsIn(amount, token_address_path).call()[0]
        amount_in = int(amount_in * (1 + slippage))
        tx = contract.functions.swapTokensForExactETH(
            amount, amount_in,
            [token_address_path[0], token_address_path[1]],
            from_address,
            int(time.time()) + 1000000).buildTransaction({
                'chainId': self.chain_id,
                'gas': gas,
                'gasPrice': self.get_gas_price(self.network),
                'nonce': nonce,
        })
        await self.send_tx_contract_transaction(nonce=nonce, from_address_pub_key=from_address,
                                                from_address_pri_key=from_address_pri_key,
                                                smart_contract_address=smart_contract_address,
                                                tx_data=tx['data'])

    @process
    async def swap_exact_tokenA_for_tokenB(self, smart_contract_address: str, contract: Contract,
                                           nonce: int, from_address: str, from_address_pri_key: str,
                                           amount: int, token_address_path: list, slippage: float = 0.001,
                                           gas: int = 210000):
        """
        出售固定数量的代币(交换得到tokenB的数量不固定）
        """
        amount_out = contract.functions.getAmountsOut(amount, token_address_path).call()[1]
        amount_out = int(amount_out * (1 - slippage))
        tx = contract.functions.swapExactTokensForTokens(
            amount, amount_out,
            [token_address_path[0], token_address_path[1]],
            from_address,
            int(time.time()) + 1000000).buildTransaction({
                'chainId': self.chain_id,
                'gas': gas,
                'gasPrice': self.get_gas_price(self.network),
                'nonce': nonce,
        })
        await self.send_tx_contract_transaction(nonce=nonce, from_address_pub_key=from_address,
                                                from_address_pri_key=from_address_pri_key,
                                                smart_contract_address=smart_contract_address,
                                                tx_data=tx['data'])

    @process
    async def swap_tokenA_for_exact_tokenB(self, smart_contract_address: str, contract: Contract,
                                           nonce: int, from_address: str, from_address_pri_key: str,
                                           amount: int, token_address_path: list, slippage: float = 0.001,
                                           gas: int = 210000):
        """
        用(数量不固定）的TokenA交换得到对应精确数量的TokenB
        """
        amount_in = contract.functions.getAmountsIn(amount, token_address_path).call()[0]
        amount_in = int(amount_in * (1 + slippage))
        tx = contract.functions.swapTokensForExactTokens(
            amount, amount_in,
            [token_address_path[0], token_address_path[1]],
            from_address,
            int(time.time()) + 1000000).buildTransaction({
                'chainId': self.chain_id,
                'gas': gas,
                'gasPrice': self.get_gas_price(self.network),
                'nonce': nonce,
        })
        await self.send_tx_contract_transaction(nonce, from_address, from_address_pri_key,
                                                smart_contract_address,
                                                tx['data'])
