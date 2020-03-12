from math import ceil, sqrt
class Solution:
    def numSquares(self, n: int) -> int:
        if n <= 3:
            return n

        dp = [0,1,2,3]

        for i in range(4,n+1):
            dp.append(i) # at least we need i square numbers to sum up to i (all
                         # of them are 1)

            # the reason to iterate from 1 to int(ceil(sqrt(i))) + 1 instead of
            # just using int(sqrt(i)) is that, int(sqrt(i)) is not necessarily
            # the best number
            for x in range(1,int(ceil(sqrt(i))) + 1):
                temp = x*x
                if temp>i:
                    break
                else:
                    dp[i] = min(dp[i], 1 + dp[i-temp])
        return dp[n]

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]
        for i in range(1,n+1):
            candidate_list = []
            for j in range(int(sqrt(i)),0,-1):
                candidate_list.append(dp[i-j*j])
            # 1 means j*j
            dp.append(1+min(candidate_list))

        return dp[n]


# dp.append(i) means at most we have i ways (1+1+1+...)
# dp[i] shows the least number of perfect square numbers sum to i
# dp[i-temp] means that 假如我们要求12，然后temp = 9，那么还剩３，我们只需要知道dp[3]再
# 加上9代表的这个值即可
# The important thing is to find out how state transfers
