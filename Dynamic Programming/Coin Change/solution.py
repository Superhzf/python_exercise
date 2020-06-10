class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins: # Under the condition that this coin is used
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

# This is similar to Perfect Squares problem
# dp[i] means how many coins needed to sum to i udner the condition that
# a certain coin is used

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [+float('inf')] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if i-coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1

# start from enumerating all valid solutions and find the one that needs
# the least number of coins.
# Suppose amount = 11, coins = [1,2,5]
#               11
#      10       9       6
# 9     ...     ...     ...
# we can see that 9 has to be calculated two times
# 1. overlapped sub-problems
# as described above
# 2. the optimized sub-structure and state trasnformation:
# dp[i] shows that the least number of coins needs to make up i dollars
# so dp[i] = 0 if i - coin < 0 for any coin in coin list
# dp[i] = min(dp[i], dp[i-coin]+1) for any coin in the coin list
