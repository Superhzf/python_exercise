class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        lo, hi = max(weights), sum(weights) # O(N)
        while lo < hi: # O(NlogN)
            mid = (lo+hi) // 2
            if self.Enough(weights, D, mid):
                # If mid is enough to ship all goods
                hi = mid
            else:
                lo = mid + 1
        return lo

    def Enough(self,weights, D, k): # O(N)
    # Whether k is enough to ship weights within D days
        days = 1
        tank = k # tank is the conveyor's capacity
        for weight in weights:
            tank = tank - weight
            if tank < 0:
                days = days+1
                tank = k - weight
        # print('days_needed:', days)
        return days <= D
