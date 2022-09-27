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

class QQCaller:
    def __init__(self, private_key, chainid=BSC):
        self.private_key = private_key
        self.address =  Web3.toChecksumAddress(produce_wallet(private_key))
        self.chainid = chainid
        self.w3 = get_web3(chainid)

    def change_net(self, chainid):
       if(chainid != chainid):
           self.chainid = chainid
           self.w3 = get_web3(chainid)

    def transfer(self, to):
        value = self.w3.eth.get_balance(self.address)
        to = Web3.toChecksumAddress(to)
        price = self.w3.eth.gasPrice
        gas = 21000
        fee = price * gas
        print(self.address)
        print(Web3.fromWei(value, 'ether'))
        if(fee > value):
            print('not enough balance')
            return

        signed_txn = self.w3.eth.account.sign_transaction(dict(
            nonce=self.w3.eth.get_transaction_count(self.address),
            gasPrice=price,
            gas=gas,
            to=to,
            value=(value - (price * gas)),
            data=b'',
            chainId=self.chainid
            ), self.private_key)

        try:
            self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print('success')
        except Exception as e:
            print(str(e))
   
    