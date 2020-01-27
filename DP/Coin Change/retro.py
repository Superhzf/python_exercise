def coinChange(coins, amount):
    dp = [float('inf')]*amount
    dp[0] = 0 

    for coin in coins:
        for i in (coin,amount+1):
            dp[i] = min(dp[i],dp[amount-i]+1)

    return dp[amount] if dp[amount] != float('inf') else -1
