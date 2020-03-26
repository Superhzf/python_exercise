# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        res = -1
        break_out = False
        for col in range(n):
            for row in range(n):
                if knows(row,col) == 0:
                    break_out = True
                    break
            if break_out is True:
                break_out = False
                target_col = None
            else:
                target_col = col
                break
        if target_col is None:
            return -1

        for row in range(n):
            if row == target_col:
                if knows(target_col,row) != 1:
                    return -1
            else:
                if knows(target_col,row) != 0:
                    return -1
        return target_col

# I solved this problem myself
