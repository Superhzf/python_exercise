class NumArray:

    def __init__(self, nums: List[int]):
        if not nums:
            return
        self.nums = nums
        self.sum = [0]*len(nums)
        self.sum[0] = nums[0]
        for i in range(1,len(nums)):
            self.sum[i] = self.sum[i-1]+self.nums[i]

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.sum[j]
        else:
            return self.sum[j]-self.sum[i-1]

# use self.sum[i] shows the sum of nums from index 0 to index i
# if we want to know the sum from index i to index j
# just subtract self.sum[i-1] from self.sum[j]
