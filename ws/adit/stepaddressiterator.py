from ws.utils.jacobian import(  
    fast_multiply,
    fast_add,
    G
)

from .addressiterator import(
    AddressIterator
)

class StepAddressIterator(AddressIterator):
    def __init__(self, s, r, step):
        AddressIterator.__init__(self, s, r)
        step = step if step != 0 else 1
        self._step = step
        self._gs = fast_multiply(G, step)

    def next(self):
        self._g0 = fast_add(self._g0, self._gs)
        self._r = self._r + self._step