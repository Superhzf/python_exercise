class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        current_sum = nums[0]
        best_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(num,current_sum+num)
            best_sum = max(best_sum,current_sum)
        return best_sum

# The key is understand that at each step, either it starts a new series or
# the number will be added to the previous series.
# The idea is updating the best sum at each step.
