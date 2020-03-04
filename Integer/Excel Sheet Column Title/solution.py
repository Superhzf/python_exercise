class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ''
        while n>0:
            if n%26 == 0:
                r= 26
            else:
                r=n%26
            remainder = chr(64+r)
            res=remainder + res
            n = (n-r)//26
        return res


# This is like 26 jinzhi problem, but a little bit different

# Below is to convert an excel string to an integer
class Solution:
    def titleToNumber(self, s: str) -> int:
        total = 0
        num = 0
        for sub_s in s[::-1]:
            total = total+(26**num)*(ord(sub_s)-64)
            num += 1
        return total
