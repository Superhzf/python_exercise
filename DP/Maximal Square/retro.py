def maximalSquare(matrix):
    if matrix == []:
        return 0

    row = len(matrix)
    col = len(matrix[0])

    if row == 1:
        return max(matrix[0])

    if col == 1:
        return max([row[0] for row in matrix])


    dp = [[0*col] for _ in len(row)]
    max_square = 0
    for i in range(len(row)):
        dp[i][0] = int(matrix[i][0])
        if dp[i][0] != 0:
            max_square = 1

    for j in range(len(col)):
        dp[0][j] = int(matrix[0][j])
        if dp[0][j] != 0:
            max_square = 1

    for i in range(1,len(row)):
        for j in range(1,len(col)):
            if matrix[i][j] > 0:
                dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1

            if dp[i][j] * dp[i][j] > max_square:
                max_square = dp[i][j] * dp[i][j]
    return max_square
