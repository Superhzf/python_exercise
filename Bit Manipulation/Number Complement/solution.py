from math import floor
from math import log

class Solution:
    def findComplement(self, num: int) -> int:

        bits_length = floor(log(num, 2) + 1)

        return num^(2**bits_length - 1)
