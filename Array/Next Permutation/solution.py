class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = len(nums) - 2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

        nums[i+1:] = nums[i+1:][::-1]

# Step 1: find the first element i from the right such that nums[i+1] > nums[i]
# Step 2: find the largest element j from the right such that nums[j] > nums[i]
# Step 3: swap nums[i] and nums[j]
# Step 4: reverse nums[i+1:]
