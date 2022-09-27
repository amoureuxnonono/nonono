from ws.utils.jacobian import(  
    fast_multiply,
    N,
    G
)

from .addressiterator import(
    AddressIterator
)

class RevolvingAddressIterator(AddressIterator):
    def __init__(self, start: str):
        self._start = start
        self._p = len(start) - 1
        self._r = 0
        self.max = len(start)
        self.next()

    def next(self):
        self._s = (int(self._start, 16)) % N
        self._g0 = fast_multiply(G, self._s)
        start = self._start
        self._start = start[-self._p:] + start[0:1]