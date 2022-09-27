from ws.utils.jacobian import(  
    N,
    to_64hex,
    produce_wallet_int,
    produce_wallet
)

from ws.caller import (
    BatchBalancesCaller 
)

from ws.chains import(
    get_BatchBalancesAddress
)

from ws.adit import(
    StepAddressIterator,
    PowAddressIterator,
    RevolvingAddressIterator,
    FileAddressIterator,
    XLoopAddressIterator,
    YLoopAddressIterator,
    DoubleAddressIterator,
    BirthdayAddressIterator,
    RBirthdayAddressIterator
)

class BatchForceScan:
    def __init__(self, chainid, loopmax = 200):
        self._caller = BatchBalancesCaller(chainid, ca = get_BatchBalancesAddress(chainid))
        self._loopmax = loopmax
    
    def pow_scan(self, a, max):
        it = PowAddressIterator(a)
        self._loop_scan(it, max)

    def revolving_scan(self, start: str): 
        it = RevolvingAddressIterator(start)
        self._loop_scan(it, it.max)

    def xyloop_scan(self, start: int, xy = 0, max = 200):
        it = XLoopAddressIterator(start) if xy == 0 else YLoopAddressIterator(start)
        self._loop_scan(it, max)

    def multiply_scan(self, start: int, max = 200):
        self.step_scan(start, start, max)

    def double_scan(self, start: int, max = 200):
        it = DoubleAddressIterator(start)  
        self._loop_scan(it, max)

    def birthday_scan(self, prefix = '', suffix = '', max = 200):
        it = BirthdayAddressIterator(prefix, suffix)  
        self._loop_scan(it, max)

    def file_scan(self, dict_path: str):
        it = FileAddressIterator(dict_path)
        self._loop_scan(it, it.max)

    def rbirthday_scan(self, max = 200):
        it = RBirthdayAddressIterator()  
        self._loop_scan(it, max)

    def step_scan(self, start, step, max):
        it = StepAddressIterator(start, 0, step)
        self._loop_scan(it, max)

    def _loop_scan(self, it, max):
        index = 0
        while index < max:
            _max = max - index 
            _max = _max if _max < self._loopmax else self._loopmax
            self._execute_batchscan(it, _max)
            index = index + self._loopmax
             
    def _execute_batchscan(self, it, max):
        wallets = []
        index = 0
        while index < max:
            index = index + 1
            self._execute_scan(it, wallets)
            it.next()
        self._do_scan(wallets)    

    def _execute_scan(self, it, wallets):
        wallets.append((it.get_current_address(),  it.get_current_privatekey()))
        wallets.append((it.get_current_halfadd_address(),  it.get_current_halfadd_privatekey()))
        wallets.append((it.get_current_minus_address(),  it.get_current_minus_privatekey()))
        wallets.append((it.get_current_halfminus_address(),  it.get_current_halfminus_privatekey()))

    def _do_scan(self, wallets):
        addresses = []
        for wallet in wallets:
            addresses.append(wallet[0])

        balances = self._caller.find(addresses)
        index = 0
        while index < len(balances):
            value = self._caller.fromWei(balances[index])
            if(value > 0):
                print('key = ' + wallets[index][1] + ' wallet = ' + wallets[index][0] + ' balance = ' + str(self._caller.fromWei(balances[index])))
            index = index + 1