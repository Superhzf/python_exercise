from math import sqrt
def numSquares(n):
    if n <= 3:
        return n

    dp = [0,1,2,3]
    for i in range(4,n+1):
        dp.append(i)

        for j in range(1,int(sqrt(i))+1):
            temp = j*j
            if temp > i:
                break
            else:
                dp[i] = min(dp[i],dp[i-temp]+1)
    return dp[-1]
