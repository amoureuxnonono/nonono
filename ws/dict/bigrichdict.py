import os

class BigRichDict:
    def __init__(self, dict_path):
        self.dict = {}
        with open(dict_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                input = line.rstrip('\n')
                key = int(input, 16)
                y = self.dict.get(key, -1)
                if(y == -1):
                    self.dict[key] = 1
                 
    def check(self, w: int) -> bool:
        return self.dict.get(w, -1) == 1