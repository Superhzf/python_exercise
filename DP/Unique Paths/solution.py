class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        if m == 1 or n == 1:
            return 1

        count = [[0 for x in range(n)] for y in range(m)]

        for i in range(m):
            count[i][0] = 1

        for j in range(n):
            count[0][j] = 1

        for i in range(1,m):
            for j in range(n):
                count[i][j] = count[i-1][j] + count[i][j-1]
        return count[m-1][n-1]
