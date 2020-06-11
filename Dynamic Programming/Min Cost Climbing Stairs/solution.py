class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost[0],cost[1])

        min_cost_list = [0]*len(cost)
        min_cost_list[0] = cost[0]
        min_cost_list[1] = cost[1]
        for i in range(2,len(cost)):
            if i != len(cost)-1:
                min_cost_list[i] = min(cost[i]+min_cost_list[i-1],cost[i] + min_cost_list[i-2])
            else:
                min_cost_list[-1] = min(cost[i]+min_cost_list[i-2],min_cost_list[i-1])

        return min_cost_list[-1]

# Solution two
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        size = len(cost)
        if size <= 2:
            return min(cost)
        f1 = cost[0]
        f2 = cost[1]
        for i in range(2, size):
            curr_cost = cost[i] + min(f1,f2)
            f1 = f2
            f2 = curr_cost
        return min(f1, f2)

# f1 and f2 shows that the least cost to step through the current floor
# since we only care about the least cost to the previous two floors so
# we only need f1 and f2 instead of a DP table
