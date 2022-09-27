from ws.utils.jacobian import(  
    fast_multiply,
    N,
    G
)

from .addressiterator import(
    AddressIterator
)

class XLoopAddressIterator(AddressIterator):
    def __init__(self, start: int):
        AddressIterator.__init__(self, start, 0)
        self._x = self._g0[0]

    def next(self):
        self._s = self._x
        self._g0 = fast_multiply(G, self._s)
        self._x = self._g0[0]