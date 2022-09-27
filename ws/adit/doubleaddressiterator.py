from ws.utils.jacobian import(  
    fast_add,
    N
)

from .addressiterator import(
    AddressIterator
)

class DoubleAddressIterator(AddressIterator):
    def __init__(self, start: int):
        AddressIterator.__init__(self, start, 0)

    def next(self):
        self._s = (self._s + self._s) % N
        self._g0 = fast_add(self._g0, self._g0)