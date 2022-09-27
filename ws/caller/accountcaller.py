from web3 import Web3
 
from ws.utils.jacobian import(  
    produce_wallet
)

from ws.net import(
    get_web3
)

from ws.chains.ChainIds import (
    BSC
)

class AccountCaller:
    def __init__(self, private_key, chainid=BSC):
        self.private_key = private_key
        self.address =  Web3.toChecksumAddress(produce_wallet(private_key))
        self.chainid = chainid
        self.w3 = get_web3(chainid)

    def change_net(self, chainid):
       if(chainid != chainid):
           self.chainid = chainid
           self.w3 = get_web3(chainid)

    def balance(self):
        value = self.w3.eth.get_balance(self.address)
        return Web3.fromWei(value, 'ether')

    def nonce(self):
        return self.w3.eth.get_transaction_count(self.address)

    def transfer(self, to, amount, code=b''):
        value = Web3.toWei(amount, 'ether')
        to = Web3.toChecksumAddress(to)
        signed_txn = self.w3.eth.account.sign_transaction(dict(
            nonce=self.w3.eth.get_transaction_count(self.address),
            gasPrice=self.w3.eth.gasPrice,
            gas=100000,
            to=to,
            value=value,
            data=code,
            chainId=self.chainid
            ), self.private_key)

        try:
            self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print('success')
        except Exception as e:
            print(str(e))

    def create(self, code):
        signed_txn = self.w3.eth.account.sign_transaction(dict(
            nonce=self.w3.eth.get_transaction_count(self.address),
            gasPrice=self.w3.eth.gasPrice,
            gas=8000000,
            data=code,
            chainId=self.chainid), self.private_key)
        try:
            self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print('success')
        except Exception as e:
            print(str(e))
 
    
   
    