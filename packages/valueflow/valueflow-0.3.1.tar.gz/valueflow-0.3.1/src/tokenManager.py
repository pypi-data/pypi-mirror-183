import asyncio

from src.sendToken import SendToken


def connect_mainnet(func):
    def wrapper(self, *args, **kwargs):
        count = 0
        while 1:
            if self.w3.isConnected():
                break
            count += 1
            if count == 10:
                raise Exception("无法连接当前主网")
        return func(self, *args, **kwargs)

    return wrapper


class TokenManger(SendToken):
    @connect_mainnet
    def distribute_mainnet_token(self, send_amount: float, from_address: str, from_address_pri_key: str,
                                 to_address_list: list, eip1559: bool = False):
        """
        一对多分发主网代币
        :param send_amount: 发送代币数量
        :param from_address: 发送地址
        :param from_address_pri_key: 发送地址私钥
        :param to_address_list: 接收地址公钥列表
        :param eip1559: 是否按eip1559发送交易
        """
        send_amount = self.w3.toWei(send_amount, 'ether')
        for to_address in to_address_list:
            asyncio.run(self.send_token(send_amount, to_address, from_address, from_address_pri_key, eip1559=eip1559))

    @connect_mainnet
    def distribute_smart_contract_token(self, send_amount: float, from_address: str, from_address_pri_key: str,
                                        to_address_list: list,
                                        smart_contract_address: str,
                                        abi: list, eip1559: bool = False):
        """
        一对多分发智能合约代币
        :param send_amount: 发送代币数量
        :param from_address: 发送地址
        :param from_address_pri_key: 发送地址私钥
        :param to_address_list: 接收地址公钥列表
        :param smart_contract_address: 智能合约地址
        :param abi: 智能合约abi
        :param eip1559: 是否按eip1559发送交易
        """
        for to_address in to_address_list:
            asyncio.run(
                self.send_contract_token(send_amount, to_address, from_address, from_address_pri_key,
                                         smart_contract_address,
                                         abi, eip1559=eip1559)
            )

    @connect_mainnet
    def withdraw_other_account_mainnet_token(self, account_dict: dict, to_address: str, eip1559: bool = False):
        """
        多对一，回收其他账户的主网代币
        :param account_dict: 存储公私钥账户字典
        e.g. {'public_key': private_key',}
        :param to_address: 接收地址公钥
        :param eip1559: 是否按eip1559发送交易
        """
        loop = asyncio.get_event_loop()
        task = [asyncio.ensure_future(self.send_token(0, to_address, pub_key, pri_key, eip1559)) for
                pub_key, pri_key
                in
                account_dict.items()]
        loop.run_until_complete(asyncio.wait(task))
        loop.close()

    @connect_mainnet
    def withdraw_other_account_smart_contract_token(self, to_address: str, account_dict: dict,
                                                    smart_contract_address: str,
                                                    abi: list, eip1559: bool = False):
        """
        多对一全回多余账户的所有智能合约代币
        :param to_address: 接收地址公钥
        :param account_dict: 存储公私钥账户字典
        e.g. {'public_key': private_key',}
        :param smart_contract_address: 智能合约地址
        :param abi: 智能合约ABI
        :param eip1559: 是否按eip1559发送交易
        """
        loop = asyncio.get_event_loop()
        task = [asyncio.ensure_future(
            self.send_contract_token(0, to_address, pub_key, pri_key, smart_contract_address, abi, eip1559)
        ) for
            pub_key, pri_key
            in
            account_dict.items()]
        loop.run_until_complete(asyncio.wait(task))
        loop.close()
