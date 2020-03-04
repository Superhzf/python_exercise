class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = int(a,2)
        y = int(b,2)

        while y:
            answer = x^y # XOR is x+y without considering carry items
            carry=(x&y)<<1
            x= answer
            y=carry

        return bin(x)[2:]
