class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        min1 = 2**32
        min2 = 2**32
        max1 = -2**32
        max2 = -2**32
        max3 = -2**32

        for num in nums:
            if num<min1:
                min2 = min1
                min1 = num
            elif num <= min2:
                min2 = num

            if num>=max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num>=max2:
                max3=max2
                max2=num
            elif num>=max3:
                max3 = num

        return max(min1*min2*max1,max1*max2*max3)

# We only have to traverse nums once and find out
# min1 min2 max1 max2 and max3
