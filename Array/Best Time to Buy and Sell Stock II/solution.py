class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for index,_ in enumerate(prices[:-1]):
            if prices[index+1] > prices[index]:
                profit += prices[index+1] - prices[index]
        return profit

"""
instead of looking for every peak following a valley, we can simply go on crawling
over the slope and keep on adding the profit obtained from every consecutive transaction.
In the end,we will be using the peaks and valleys effectively,
but we need not track the costs corresponding to the peaks and valleys
along with the maximum profit, but we can directly keep on adding the difference
between the consecutive numbers of the array if the second number is larger
than the first one, and at the total sum we obtain will be the maximum profit.

[1, 7, 2, 3, 6, 7, 6, 7]

"""
