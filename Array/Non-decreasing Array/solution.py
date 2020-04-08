class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        p = None
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                if p is not None:
                    return False
                p = i

        return (p is None or p == 0 or p == len(nums)-2 or
                nums[p-1] <= nums[p+1] or nums[p] <= nums[p+2])

# nums[p-1] <= nums[p+1]： should hold if we remove nums[p] [-1,4,2,3]
# nums[p] <= nums[p+2]：should hold if we remove nums[p+1] [2,3,3,2,4]
