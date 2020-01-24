class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        if digits[-1] != 9:
            digits[-1] = digits[-1]+1
            return digits
        elif digits == [9]*n:
            return [1]+[0]*n
        else:
            digits[-1] = 0
            count = n - 1
            for i in digits[n-2::-1]:# 从倒数第二个遍历到第一个
                count-=1
                if i<9:
                    digits[count] = digits[count]+1
                    break
                elif i == 9: # [8,9,9,9]
                    digits[count] = 0
            return digits
