class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 0:
            return
        if len(cost) == 1:
            return cost[0]
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


# I successfully solved this problem myself
# I just want to say that this problem is pretty much the same as House Robber problem.
# So, the bottom line here is to truely understand this kind of problem
