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

# we can split this problem into several basic problems,
# if we want to reach table[i][j], we can reach from table[i-1][j] or table[i][j-1],
# so, as long as we know table[i-1][j] and table[i][j-1], problem solved.
# To me, the key is that we have to realize that the # of ways to reach table[0][j] == 1
# and the number of ways to reach table[i][0] == 1
