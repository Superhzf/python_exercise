class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        visited_index = [] # All the visited index no matter it is the starting point or not
        size = len(nums)
        for curr_pos, num in enumerate(nums):
            if curr_pos in visited_index: # We plan to visit all the index
                continue
            this_cycle = [] # It will store index for this cycle
            while num*nums[curr_pos]>0: # Alway move to the same direction
                if curr_pos in this_cycle:
                    if this_cycle[-1]!=curr_pos:
                        return True # The length of the cycle is larger than 1
                    else:
                        break
                this_cycle.append(curr_pos)
                visited_index.append(curr_pos)
                curr_pos = (curr_pos+nums[curr_pos])%size
        return False
