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

# Step 1: create a list to store all visited index
# Step 2: Iterate nums and make sure it is not in the list created in step 1
# Step 3: In each iteration, make sure that we are always moving forward or backward
# Step 4: In each iteration, if we reach the same index before, if the cycle length
# is larger than 1, then return True, else store this index to the list for this
# cycle and store the index to the visited_index list too
