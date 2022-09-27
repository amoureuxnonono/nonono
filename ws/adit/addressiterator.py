from ws.utils.jacobian import(
    N,
    P,
    G,
    inv,
    fast_multiply,
    fast_add,
    towallet,
    to_64hex
)

class AddressIterator:
    _U = inv(2, N)
    _Gu = fast_multiply(G, _U)

    def __init__(self, s, r):
        self._s = s
        self._r = r
        self._g0 = fast_multiply(G, (s + r))

    def get_current_address(self):
        return towallet(self._g0)

    def get_current_privatekey(self):
        return to_64hex((self._s + self._r) % N)

    def get_current_halfadd_address(self):
        g1 = fast_add(AddressIterator._Gu, self._g0)
        return towallet(g1)

    def get_current_halfadd_privatekey(self):
        return to_64hex((self._s + self._r + AddressIterator._U) % N)

    def get_current_minus_address(self):
        g1 = (self._g0[0], P - self._g0[1])
        return towallet(g1)

    def get_current_minus_privatekey(self):
        return to_64hex((N - self._s - self._r) % N)

    def get_current_halfminus_address(self):
        g1 = (self._g0[0], P - self._g0[1])
        g1 = fast_add(AddressIterator._Gu, g1)
        return towallet(g1)

    def get_current_halfminus_privatekey(self):
        return to_64hex((N - self._s - self._r + AddressIterator._U) % N)
