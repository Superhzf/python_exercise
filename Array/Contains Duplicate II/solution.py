class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_index_dict = {}
        for index,num in enumerate(nums):
            if num not in num_index_dict.keys():
                num_index_dict[num]=index
            else:
                if index-num_index_dict[num]<=k:
                    return True
                else:
                    num_index_dict[num] = index
        return False
# dynamic programming:
# 把每个元素的位置记录在dict中方便后面遇到相同元素的时候查询index的差值
