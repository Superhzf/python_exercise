class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False

        return n & (-n) == n

# This is a O(1) solution
# The ieda is that -n is shown by using the two's complement of n, n and -n will
# share the rightmost 1-bit and sets all the others to 0.
# If n is the power of 2, it will look like '1' plus some zeros
