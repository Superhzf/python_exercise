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
# dp[i][j] means longest common subquence between text1[:i] and text2[:j]
# For example, text1 = 'abcde', text2 = 'ace'
#     a b c d e
#   0 0 0 0 0 0
# a 0 1 1 1 1 1
# c 0 1 1 2
# d 0
