class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_dict = {}

        for index,num in enumerate(nums):
            if target - num in hash_dict:
                return [index,hash_dict[target-num]]
            hash_dict[num] = index
        
