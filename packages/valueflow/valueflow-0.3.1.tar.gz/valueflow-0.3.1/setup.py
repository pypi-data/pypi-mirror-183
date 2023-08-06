from setuptools import setup

setup(
    name='valueflow',
    version='0.3.1',
    description='evm tools basis on web3.py',
    url='https://github.com/valueflowever/valueflow',
    author='y',
    packages=["src", "conf"],
    license="MIT Licence",
    install_requires=['web3==5.31.1', 'websockets==9.1', 'requests==2.25.1', 'PyYAML==5.4.1'],
    python_requires=">=3.6"
)
