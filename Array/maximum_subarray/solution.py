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
