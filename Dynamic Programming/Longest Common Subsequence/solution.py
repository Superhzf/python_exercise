class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 == text2:
            return len(text1)

        if len(text1) == 0 or len(text2) == 0:
            return 0

        dp = [[0 for j in range(len(text1)+1)] for i in range(len(text2)+1)]

        for i in range(1,len(text2)+1):
            for j in range(1,len(text1)+1):
                if text2[i-1] == text1[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])

        return dp[-1][-1]
 # we start from enumerating all valid solutions:
 #          s1 = abcde s2 = ace
 #     s1 = abcd s2 = ac
 # abc, ac          abcd a
 #  ab a               abc a
 #   ...                  ab a
 # so, we have to calculate the LCS between 'ab' and 'a' twice
 # we can see that 7 has to be calculated two times
 # 1. overlapped sub-problems
 # 2. the optimized sub-structure and state trasnformation:
 # dp[i][j] shows that LCS between s1[:i] and s2[:j]
 # dp[i][j] = dp[i-1][j-1] if s[i] == s[j]
 # dp[i][j] = max(dp[i-1][j], dp[i][j-1]) else
 
