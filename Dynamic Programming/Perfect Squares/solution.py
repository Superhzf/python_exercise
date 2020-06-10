from math import sqrt
class Solution:
    def numSquares(self, n: int) -> int:

        dp = [0] * (n+1)
        for i in range(1, n+1):
            dp[i] = i

        for i in range(1, n+1):
            candidate_list = []
            for j in range(int(math.sqrt(i))+1):
                candidate_list.append(dp[i-j*j])
            dp[i] = min(dp[i], 1+min(candidate_list))
        return dp[n]

# we start from enumerating all valid solutions:
#               12
#       11      8       3
#   10, 7, 2   7, 4
# we can see that 7 has to be calculated two times
# 1. overlapped sub-problems
# as described above
# 2. the optimized sub-structure and state trasnformation:
# dp[i] shows the least # of perfect squares numbers needed
# dp[i] = dp[i-j*j] for j in range(sqrt(i)+1)
