class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 0:
            return 0
        n = len(prices)
        dp = [[0]*2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], -prices[i])
        return dp[n-1][0]
# This is the classic dynamic programming solution
# dp[i][j] shows that ith day do j operation, j=0 means sell, j=1 means buy
# the key is to iterate different operations in the same day.

# three essential elements of DP:
# 1.overlapped sub-problems
# If I want to know the profit to sell at ith day, I have to calculate
# the profit to sell at (i-1)th day, (i-1)th day and make comparison.
# 2.the optimized sub-structure:
# if I know dp[i-1][0] and dp[i-1][1],
# then dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
# 3. state transformation:
# dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
# dp[i][1] = max(dp[i-1][1], -prices[i])

# Obviously, we only need to keep the status of the previous day, so:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 0:
            return 0
        n = len(prices)
        i_sell = 0
        i_buy = -prices[0]
        for i in range(1, n):
            i_sell = max(i_sell, i_buy+prices[i])
            i_buy = max(i_buy, -prices[i])
        return i_sell
