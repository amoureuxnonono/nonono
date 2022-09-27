from ws.utils.jacobian import(  
    fast_multiply,
    G
)

from .addressiterator import(
    AddressIterator
)

import codecs
from web3 import Web3

class FileAddressIterator(AddressIterator):
    def __init__(self, dict_path: str):
        self._dict = []
        with open(dict_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                key = line.rstrip('\n').strip()
                if(len(key) > 0):
                    self._dict.append(key)
        
        self._current_index = 0
        self._max_index = len(self._dict) - 1
        self.max = self._max_index + 1
        AddressIterator.__init__(self, self.__get_current_hash(), 0)

    def __get_current_str(self):
        if(self._current_index > self._max_index):
            return ''
        return self._dict[self._current_index]

    def __get_hash(self, value):
        n = Web3.toBytes(text = value)
        private_key_bytes = Web3.solidityKeccak(['bytes'], [n])
        hash = codecs.encode(private_key_bytes, 'hex')
        return int(hash, 16)

    def __get_current_hash(self):
        value = self.__get_current_str()
        return self.__get_hash(value)

    def next(self):
        self._current_index = self._current_index + 1
        self._s = self.__get_current_hash()
        self._g0 = fast_multiply(G, self._s)