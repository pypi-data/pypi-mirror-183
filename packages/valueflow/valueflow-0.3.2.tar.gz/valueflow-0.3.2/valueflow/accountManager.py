from eth_account import Account
import yaml
import os
import configparser


def create_account(num: int) -> dict:
    """
    创建账户
    :param num: 生成的账户数量
    :return: 生成的账户列表 {公钥: 私钥}
    """
    account_dict = {}
    for i in range(num):
        acc = Account.create()
        pub_key = acc.address
        pri_key = acc.key.hex()
        if pub_key not in account_dict:
            account_dict[pub_key] = pri_key
    return account_dict


def export_account(filename: str, num: int):
    """
    导出账户
    :param filename: 存放的文件名
    :param num: 生成的账户数量
    """
    if '.yml' not in filename:
        filename = f'{filename}.yml'
    create_account_dict = create_account(num)
    if os.path.exists(filename):
        try:
            with open(filename) as f:
                config = yaml.load(f, Loader=yaml.FullLoader)
                account_dict = config['DEFAULT']['WALLET_ACCOUNT']
                account_message = dict(account_dict, **create_account_dict) if account_dict else create_account_dict
                write_yaml(filename, account_message)
        except TypeError:
            write_yaml(filename, create_account_dict)
    else:
        write_yaml(filename, create_account_dict)


def get_account(filename: str) -> dict:
    """
    读取yml文件账户的公私钥
    :param filename: 文件名
    :return: 公私钥字典 {'public_key': 'private_key', ... }
    """
    if '.yml' not in filename:
        filename = f'{filename}.yml'
    with open(filename) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        return config['DEFAULT']['WALLET_ACCOUNT']


def write_yaml(filename: str, account_message: dict):
    """
    按设定好的格式写入 yml 文件
    :param filename: 文件名
    :param account_message: 公私钥存放的字典
    """
    desired_caps = {
        'DEFAULT': {
            'WALLET_ACCOUNT': account_message
        }
    }
    if '.yml' not in filename:
        filename = f'{filename}.yml'
    with open(f'{filename}', 'w', encoding="utf-8") as f:
        yaml.dump(desired_caps, f)


def get_config(filepath: str) -> dict:
    """
    读取账号配置信息
    :param filepath: 文件路径
    """
    config = configparser.ConfigParser()
    config.read(filepath, encoding='utf-8-sig')
    items = config._sections
    items = dict(items)
    for item in items:
        items[item] = dict(items[item])
    return items
