class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums), 2):
			# O(1)
            max_val = max(nums[i - 1:i + 2])
			# Center is the max val
            if nums[i] == max_val:
                continue
            if nums[i - 1] == max_val:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
            elif i < len(nums) - 1:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

# scan through the indices you know will have to be "mountains" and force them to be so.
# In every window there will only be 3 numbers, you are guaranteed to pass test cases
# if you put the max of the window in the middle of the said window.
# Thus, find the max, check if it is in the middle, if not,
# find out if left or right are the max, then execute the swap in place.
