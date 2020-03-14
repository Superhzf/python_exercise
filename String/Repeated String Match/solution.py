import math

class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        if not set(B).issubset(set(A)):
                return -1

        base = math.ceil(len(B) / len(A)) # this is to find how many times
                                          # A should be copied to be longer
                                          # than B
        for i in range(2):
            if B in A*(base + i):
                return base + i
        return -1

#
