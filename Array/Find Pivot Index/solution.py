class Solution(object):
    def pivotIndex(self, nums):
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1

# Step 1: calculate the total sum and initiate the left sum as 0
# Step 2: Iterate each element in nums, calculate whether left sum and right sum
# is equal to each other
