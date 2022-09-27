from ws.utils.jacobian import(  
    fast_multiply,
    N
)

from .addressiterator import(
    AddressIterator
)

class PowAddressIterator(AddressIterator):
    def __init__(self, a):
        AddressIterator.__init__(self, a, 0)
        self._pow = a

    def next(self):
        self._s = (self._s * self._pow) % N
        self._g0 = fast_multiply(self._g0, self._pow)