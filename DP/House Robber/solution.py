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

# While reaching house i thief has two options, either he robs it or leave it.
# Let dp[i] represents the maximum value stolen so far on reaching house i.
# We can calculate the value of dp[i] as following
# dp[i] = max (nums[i] + dp[i-2], dp[i-1])
