def maxProfit(prices):
    profit = 0
    for index,price in enumerate(prices[:-1]):
        if prices[index]<prices[index+1]:
            profit = prices[index+1] - prices[index]
    return profit
