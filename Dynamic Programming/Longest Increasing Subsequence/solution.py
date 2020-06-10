class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return 1
        dp = [1] * n

        max_len = 0
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            if dp[i] > max_len:
                max_len = dp[i]
        return max_len

# Start from enumerating all valid solutions. Suppose the nums is
# [10,9,2,5,3,7,101,18], if we want to know the LIS at 18
# then we have to know the list ending with 7, 3, 5, 2 9, 10 since they are
# smaller than 18. In order to do get the list, we have to know the list
# ending with 9, so 9 has to be calculated two times.
# 1. overlapped sub-problems
# as described above
# 2. the optimized sub-structure and state trasnformation:
# dp[i] shows that LIS ended with nums[i], it is not necessarily to be the
# global optimal solution, so  we have to keep track of the best solution.
