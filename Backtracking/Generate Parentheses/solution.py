class Solution:
    def generateParenthesis(self, N: int) -> List[str]:

        def backtrack(S = '', opening = 0, closing = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return

            if opening < N:
                backtrack(S+'(',opening + 1, closing)
            if closing < opening:
                backtrack(S+')',opening, closing + 1)

        ans = []
        backtrack()
        return ans
# The idea is that only add them when we know it will remain a valid sequence.
# We can do this by keeping track of the number of opening and closing brackets
# we have placed so far. This is not a standard backtracking problem because we
# do not check validation.

# Time complexity:
# The way I like to think about the runtime of backtracking algorithms is O(b^d),
# where b is the branching factor and d is the maximum depth of recursion.
# Backtracking is characterized by a number of decisions b that can be made at
# each level of recursion. If you visualize the recursion tree, this is the number
# of children each internal node has. You can also think of b as standing for "base",
# which can help you remember that b is the base of the exponential. If we can
# make b decisions at each level of recursion, and we expand the recursion tree
# to d levels (i.e. each path has a length of d), then we get b^d nodes.
# Since backtracking is exhaustive and must visit each one of these nodes,
# the runtime is O(b^d).
# So, time complexity = O(2^n)

# Space complexity: O(n)
