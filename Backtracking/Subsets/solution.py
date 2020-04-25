class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def backtrack(first=0, curr=[]):
            if len(curr) == k:
                output.append(curr[:])

            for i in range(first,n):
                curr.append(nums[i])
                backtrack(i+1, curr)
                curr.pop()

        output = []
        n = len(nums)
        for k in range(n+1):
            # k: the length of the subset
            backtrack()
        return output
# The key is how to define the backracking function.
