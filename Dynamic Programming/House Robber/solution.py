class Solution:
    def rob(self, nums: List[int]) -> int:
        h_len = len(nums)
        if h_len == 0:
            return 0
        if h_len == 1:
            return nums[0]
        if h_len == 2:
            return max(nums)

        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2,h_len):
            dp[i] = max(nums[i]+dp[i-2],dp[i-1])
        return dp[-1]

# since we only care about the two cloest previous profits, so we can
# further optimize the solution
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]


        n = len(nums)

        dp_0 = nums[0]
        dp_1 = max(nums[0], nums[1])

        for i in range(2, n):
            dp_i = max(dp_1, dp_0+nums[i])
            dp_0 = dp_1
            dp_1 = dp_i
        return dp_1

# start from enumerating all the valid solutions, suppose the house list
# is nums = [1,2,3,1,5,2], if we want to arrive nums[5] with the largest profit,
# we have to know the largest profit of nums[4] and nums[3]
#               nums[5]
#       nums[4]         nums[3]
#   nums[3] ...         ...
# we can see that nums[3] has to be solved 2 times
# 1. overlapped sub-problems
# as described above
# 2. the optimized sub-structure and state trasnformation:
# dp[i] shows the largest profit arriving nums[i]
# dp[i] = max(nums[i]+dp[i-2], dp[i-1])
