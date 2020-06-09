class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = 2**32-1
        profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > profit:
                profit = price-min_price
        return profit

# The key to this problem is how to remember the order that price shows up
# The solution is we only keep the min price and also keep profit, then calculate
# profit on each price.
