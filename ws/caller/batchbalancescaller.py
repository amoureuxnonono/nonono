from web3 import Web3

from .caller import(
    Caller
)

from ws.abi import(
    BatchBalancesABI
)

from ws.chains import(
    get_BatchBalancesAddress
)

class BatchBalancesCaller(Caller):
    def __init__(self, chainid, ca = None):
        Caller.__init__(self, chainid)
        ca = ca if ca != None else get_BatchBalancesAddress(chainid)
        self._contract = self._create_contract(ca, BatchBalancesABI)
 
    def fromWei(self, value):
        return Web3.fromWei(value, 'ether')

    def find(self, wallets):
        addresses = []
        for wallet in wallets:
            addresses.append(self._check_wallet(wallet))
        return self._contract.functions.find(addresses).call()