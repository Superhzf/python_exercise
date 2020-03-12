class Solution:
    def convertToTitle(self, n: int) -> str:
        if n <= 26:
            return chr(n+64)
        res = ''
        while True:
            if n <= 26:
                res = chr(n+64)+res
                return res

            this_digit = n%26
            if this_digit!=0:
                res = chr(this_digit+64)+res
                n = n//26
            else:
                res = chr(26+64) + res
                n = n//26 - 1
