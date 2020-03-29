class Solution:
    def subarraySum(self,nums: List[int], k: int) -> int:
        count = 0
        total_sum = 0
        hash_map = {0:1} # key: sum, value: how many continuous subarrays
        size = len(nums)
        for i in range(size):
            total_sum += nums[i]
            if total_sum - k in hash_map:
                count += hash_map[total_sum - k]

            hash_map[total_sum] = hash_map.get(total_sum,0) + 1

        return count

# The key idea is that cumulative sum up to two indices is the same,
# then the elements lying in between those indices
