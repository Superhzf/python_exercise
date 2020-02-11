class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix == []:
            return 0

        row = len(matrix)
        col = len(matrix[0])


        if row == 1:
            return max(matrix[0])

        if col == 1:
            return max([this_col[0] for this_col in matrix])

        dp = [[0]*col for _ in range(row)]

        max_square = 0
        for i in range(row):
            if int(matrix[i][0]) > 0:
                max_square = 1
            dp[i][0] = int(matrix[i][0])

        for j in range(col):
            if int(matrix[0][j]) > 0:
                max_square = 1
            dp[0][j] = int(matrix[0][j])



        for i in range(1,row):
            for j in range(1,col):
                if int(matrix[i][j])>0:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                else:
                    dp[i][j] = 0
                if dp[i][j] * dp[i][j] > max_square:
                    max_square = dp[i][j] * dp[i][j]
        return max_square

# use dp to show length of the maximum square whose bottom right corner is the
# cell with index (i,j) in the original matrix.
# dp(i,j)=min(dp(i−1,j),dp(i−1,j−1),dp(i,j−1))+1.
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
