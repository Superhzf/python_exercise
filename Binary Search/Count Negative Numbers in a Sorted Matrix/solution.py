class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        total = 0

        if grid[-1][-1] >=0 :
            return total

        row = len(grid)
        col = len(grid[0])

        pos_row = 0
        pos_col = col - 1
        while pos_row < row and pos_col >= 0:
            if grid[pos_row][pos_col] < 0:
                total = total + row - pos_row # if grid[r][c] < 0, the grid[r+1,r+2,..m][c] == 0
                pos_col -= 1
            else:
                pos_row += 1

        return total


# Consider this problem as a "staircase":
# ++++++
# ++++--
# ++++--
# +++---
# +-----
# +----
# The solution is to count - from the top right corner
# This is obviously not a binary search problem, I don't know why it is
# classified as a binary search problem per Leetcode
