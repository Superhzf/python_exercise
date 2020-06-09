class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        left = 0
        right = 0
        longest_pali = 0

        for j in range(n):
            for i in range(j):
                if s[i] == s[j] and (j-i<=1 or dp[i+1][j-1]):
                    dp[i][j] = 1
                if dp[i][j] and longest_pali< j-i+1:
                    longest_pali = j-i+1
                    left = i
                    right = j
        return s[left:right+1]
# dp[i][j] shows that whether s[i:j] is a palindrome number
# three essential elements of DP:
# 1.
# overlapped sub-problems: when j = 5, we have to check dp[3][0], when
# j = 6, we still have to check dp[3][0]
# 2.
# the optimized sub-structure: if we know whether s[i:j] is a palindrome, then
# it is easy to determine whether s[i-1:j+1] is a palindrome or not
# 3.
# state transformation:
# dp[i][j] = 1 if dp[i+1][j-1] = 1 and s[i] == s[j] else 0
