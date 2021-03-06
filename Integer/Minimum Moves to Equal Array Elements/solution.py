# Let's explain it in a clear and short manner:
# suppose there're k elements, the sum of original array is s, the minimum move is m,
# eventually all the elements become e, we know each move contributes (k-1) to the sum, so we have:
# s + (k-1)*m = k*e
# for the minimum element min, it must be added m times, i.e.
# min + m = e
# The two equations above would give us m = s - k*min
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        s = sum(nums)
        k = len(nums)
        minimum = min(nums)
        return s-k*minimum
