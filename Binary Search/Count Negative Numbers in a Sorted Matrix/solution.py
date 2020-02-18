    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        r, c, cnt = 0, n - 1, 0
        while r < m and c >= 0:
            if grid[r][c] < 0:
                cnt += m - r # if grid[r][c] < 0, the grid[r+1,r+2,..m][c] == 0
                c -= 1
            else:
                r += 1
        return cnt

# Consider this problem as a "staircase":
# ++++++
# ++++--
# ++++--
# +++---
# +-----
# +----
# The solution is to count - from the top right corner
