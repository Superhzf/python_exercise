class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return

        res,curr_min,curr_max = nums[0],nums[0],nums[0]

        for i in range(1,len(nums)):
            this_min = min(curr_max*nums[i],curr_min*nums[i],nums[i])
            this_max = max(curr_max*nums[i],curr_min*nums[i],nums[i])

            curr_max = this_max
            curr_min = this_min

            res = max(curr_max,res)
        return res

# we have to take negative product at each step
# because the product of two negatives could be positive later
# [2,3,-2,4]
