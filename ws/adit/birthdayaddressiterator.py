from ws.utils.jacobian import(  
    fast_multiply,
    G
)

from .addressiterator import(
    AddressIterator
)

import datetime

class BirthdayAddressIterator(AddressIterator):
    def __init__(self, prefix = '', suffix = ''):
        self._start = datetime.date.today()
        self._step = datetime.timedelta(days=1)
        self._prefix = prefix
        self._suffix = suffix
        AddressIterator.__init__(self, self._get_v(), 0)

    def _get_v(self):
        n = self._prefix + self._start.strftime('%Y%m%d') + self._suffix
        return int(n, 16)

    def next(self):
        self._start = self._start - self._step
        self._s = self._get_v()
        self._g0 = fast_multiply(G, self._s)