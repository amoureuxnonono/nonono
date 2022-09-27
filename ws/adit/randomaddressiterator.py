from ws.utils.jacobian import(  
    fast_multiply,
    G
)

from .addressiterator import(
    AddressIterator
)

import random

class RandomAddressIterator(AddressIterator):
    def __init__(self, min, max):
        self._min = min
        self._max = max 
        self.next()

    def next(self):
        self._s = random.randint(self._min, self._max)
        self._r = 0
        self._g0 = fast_multiply(G, self._s)
        