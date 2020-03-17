class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        next_digit = None
        while n!= 0:
            curr_digit = n&1
            if next_digit is not None:
                if next_digit != curr_digit:
                    return False
            next_digit = 1 - curr_digit
            n = n>>1
        return True

# I solved this problem by myself
# Just write down my solution
