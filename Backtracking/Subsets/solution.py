class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def backtrack(first = 0):
            if len(curr) == k:
                output.append(curr[:])
                return
            for i in range(first, len(nums)):
                curr.append(nums[i])
                backtrack(i+1)
                curr.pop()

        output = []
        curr = []
        for k in range(len(nums) + 1):
            backtrack()
        return output

# The key is how to define the backracking function.
