class Solution:
    def threeSumSmaller(self,nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums)-2):
            count += self.getTripletCount(nums, target - nums[i], i)
        return count

    def getTripletCount(self, nums, target, first):
        left = first+1
        right = len(nums)-1
        count = 0
        while left < right:
            if nums[left] + nums[right] < target:
                # The combination is (nums[i], nums[left], nums[left+1]),
                # (nums[i], nums[left], nums[left+2]) ...
                # (nums[i], nums[left], nums[right-1])
                # the total count is right-left
                count+=right-left
                left+=1
            else:
                right-=1
        return count

# Step 1: sort nums
# Step 2: suppose the combination includes i (i < len(nums) - 2)
# Step 3: find how many combinations are based on the condition that the combination
# includes nums[i] using function getTripletCount
# getTripletCount(nums, target, first):
# Start from first (index) of num, how many combinations in nums such that
# nums[first] + xxx + xxx is less than target
