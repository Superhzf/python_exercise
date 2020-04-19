class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        freq_map = Counter(nums)
        hype_map = Counter()

        for num in nums:
# if the number already has a place in a sequence
            if freq_map[num] == 0:
                continue

# if the number may be placed as a continuation of another sequence
            elif hype_map[num] > 0:
                hype_map[num] -= 1
                hype_map[num + 1] += 1

# the number is not consecutive to a previous sequence
# a new sequence must be created
            elif freq_map[num + 1] > 0 and freq_map[num + 2] > 0:
                freq_map[num + 1] -= 1
                freq_map[num + 2] -= 1
                hype_map[num + 3] += 1

# if the number cannot continue a new sequence
# and cannot begin a new sequence then the list
# cannot be split
            else:
                return False
            freq_map[num] -= 1

        return True
