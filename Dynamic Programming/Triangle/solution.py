class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        dp = [0] * N

        dp[0] = triangle[0][0]

        for i in range(2,N+1): # which layer of the triangle
            for j in range(i): # each element in that layer
                p1 = float('inf') if j == 0 else dp[j-1] # j==0: the first element of the ith layer
                p2 = float('inf') if j == i - 1 else dp[j] # j==i-1, the last element of the ith layer

                if j > 0:
                    dp[j-1] = tmp

                tmp = min(p1,p2) + triangle[i-1][j]

            dp[i-1] = tmp

        return min(dp)


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        row = len(triangle) - 1
        while row > 0:
            for i in range(row):
                triangle[row - 1][i] += min(triangle[row][i], triangle[row][i+ 1])
            row -= 1
        return triangle[0][0]

# 1.Bottom-up,
# 2.same col, row length
# 3.modify the original triangle
# we start from enumerating all potential solutions: from bottom to up:
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# g[i][j] means the minimum sum path arriving matrix[i][j]
#               g[0][0]
#       g[1][0]        g[1][1]
#   ... g[2][1] ...           ...   g[2,1] ...
# So, matrix[2][1] has to be calculated twice.
# 1. overlapped sub-problems
# as described above
# 2. the optimized sub-structure and state trasnformation:
# triangle[i][j] shows that the minimum sum path arriving matrix[i][j]
# so triangle[row - 1][i] += min(triangle[row][i], triangle[row][i+ 1])
