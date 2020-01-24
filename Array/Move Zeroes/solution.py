class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return
        if len(nums) == 1:
            return nums

        lastZeroFoundAt = 0
        for index,num in enumerate(nums):
            if nums[index] != 0:
                # swap nums[index] and nums[lastZeroFoundAt]
                nums[lastZeroFoundAt], nums[index] = nums[index], nums[lastZeroFoundAt]
                lastZeroFoundAt+=1
# this method is fast for consecutive zeros
# [1,0,0,3,12]->[1,0,0,3,12]->[1,3,0,0,12]->[1,3,12,0,0]
