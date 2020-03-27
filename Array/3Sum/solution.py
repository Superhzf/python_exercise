class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        i = 0
        result = []
        while i < len(nums) and nums[i] <= 0:
            dic = {}
            # We want the sum of three numbers to be 0, it is equal to
            # find out the sum of two numbers equal to a target
            target = - nums[i]
            j = i + 1
            while j < len(nums):
                if nums[j] in dic:
                    idx = dic[nums[j]]
                    result.append([nums[i], nums[idx], nums[j]])
                    while i < len(nums) - 1 and nums[i] == nums[i+1]:
                        i += 1
                    while j < len(nums) - 1 and nums[j] == nums[j+1]:
                        j += 1
                else:
                    # key means the key plus a number can be equal to target
                    # value j is the index of the number
                    dic[target - nums[j]] = j
                j += 1
            i += 1
        return result
