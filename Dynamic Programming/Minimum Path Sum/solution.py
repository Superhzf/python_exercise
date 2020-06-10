class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        if row == 1:
            return sum(grid[0])
        if col == 1:
            return sum([this_col[0] for this_col in grid])

        dp = [[0]*col for _ in range(row)]

        dp[0][0] = grid[0][0]

        for i in range(1,row):
            dp[i][0] = grid[i][0]+dp[i-1][0]

        for j in range(1,col):
            dp[0][j] = grid[0][j]+dp[0][j-1]

        for i in range(1,row):
            for j in range(1,col):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i][j]


        return dp[-1][-1]

# Start from enumerating all valid solutions:
# Suppose the grid is a 5*4 matrix, so to arrive grid[5][4]
#                       grid[5][4]
#       grid[5][3]                  grid[4][4]
#   grid[4][3]  grid[5][2]      grid[3][4]        grid[4][3]
# we can see that we have to solve grid[4][3] twice.
# 1. overlapped sub-problems
# as described above
# 2. the optimized sub-structure and state trasnformation:
# dp[i][j] shows the least sum of numbers to arrive grid[i][j],
# dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i][j]
