class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums)==3:
            return nums[0]*nums[1]*nums[2]

        min1 = 2**32-1
        min2 = 2**32-1
        max1 = -2**32-1
        max2 = -2**32-1
        max3 = -2**32-1

        for num in nums:
            if num <= min1:
                min2 = min1
                min1 = num
            elif num<=min2:
                min2 = num

            if num>=max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num>=max2:
                max3 = max2
                max2 = num
            elif num>=max3:
                max3 = num
        return max(min1*min2*max1,max1*max2*max3)

# Sorting and then find the largest 3 number is not the best answer
# We just have to iterative the list once, so time complexity is O(n), extra space
# is O(1)
