import math
class Solution:
    def numPairsDivisibleBy60(self,time: List[int]) -> int:
        hash_dict = {}
        count = 0
        for this_time in time:
            if this_time%60 in hash_dict:
                hash_dict[this_time%60] += 1
            else:
                hash_dict[this_time%60] = 1

        hash_dict_copy = {k:v for k,v in hash_dict.items()}
        for key, _ in hash_dict_copy.items():
            if 60-key in hash_dict or key == 0:
                if key == 0 or (key == 30 and hash_dict[key] >= 2):
                    this_count = hash_dict[key]
                    count = count + (this_count*(this_count-1))//2
                    del hash_dict[key]
                elif key != 30:
                    count = count + hash_dict[60-key]*hash_dict[key]
                    del hash_dict[60-key]
                    del hash_dict[key]
        return count

# I figured out this problem myself
# just want to write it down.
