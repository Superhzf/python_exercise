class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        ans = 0
        row = len(grid)
        col = len(grid[0])
        for this_row in range(row):
            for this_col in range(col):
                if (this_row,this_col) not in seen and grid[this_row][this_col] == 1:
                    this_area = 0
                    stack = [(this_row,this_col)]
                    seen.add((this_row,this_col))
                    while len(stack) > 0:
                        r, c = stack.pop()
                        this_area += 1
                        for nr,nc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                            if nr >= 0 and nr < row and nc >= 0 and nc < col and grid[nr][nc] == 1 and (nr,nc) not in seen:
                                stack.append((nr,nc))
                                seen.add((nr,nc))
                    ans = max(ans,this_area)

        return ans

# The key idea is simulating the whole proess
