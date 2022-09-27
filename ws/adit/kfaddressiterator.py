from ws.utils.jacobian import(  
    fast_multiply,
    G
)

from ws.kf.pkeys import(
    KeysFactory
)

from .addressiterator import(
    AddressIterator
)

class KFAddressIterator(AddressIterator):
    def __init__(self, count):
        self._count = count if count > 0 else 1
        self._kf = KeysFactory()
        self.next()

    def next(self):
        self._s = int(self._kf.produce(self._count), 16)
        self._r = 0
        self._g0 = fast_multiply(G, self._s)
        