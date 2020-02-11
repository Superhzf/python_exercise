def uniquePaths(m, n):
    if m == 1 or n == 1:
        return 1

    count = [[0]*n for _ in range(m)]

    for i in range(m):
        count[i][0] = 1

    for j in range(n):
        count[0][j] = 1

    for i in range(1,m):
        for j in range(1,n):
            count[i][j] = count[i-1][j] + count[i][j-1]
    return count[-1][-1]
