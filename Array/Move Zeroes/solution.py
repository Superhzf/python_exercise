class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return
        if len(nums) == 1:
            return nums

        lastNonZeroFoundAt = 0
        for index,num in enumerate(nums):
            if nums[index] != 0:
                nums[lastNonZeroFoundAt], nums[index] = nums[index], nums[lastNonZeroFoundAt]
                lastNonZeroFoundAt+=1
# this method is fast for consecutive members
