from ws.utils.jacobian import(  
    fast_multiply,
    N,
    G
)

from .addressiterator import(
    AddressIterator
)

class YLoopAddressIterator(AddressIterator):
    def __init__(self, start: int):
        AddressIterator.__init__(self, start, 0)
        self._y = self._g0[1]

    def next(self):
        self._s = self._y
        self._g0 = fast_multiply(G, self._s)
        self._y = self._g0[1]