class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        summary = []
        size = len(nums)
        j = 0
        for i in range(size):
            if i+1 < size and nums[i+1] - nums[i] == 1:
                continue
            if j == i:
                summary.append(str(nums[j]))
            else:
                summary.append(str(nums[j]) +'->'+str(nums[i]))

            j = i + 1
        return summary
