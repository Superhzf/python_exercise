# dp[i] means s[:i] can be shown using wordDict
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[0] = True

        for i in range(1,len(s)+1):
            for j in range(0,i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[len(s)]

# # three essential elements of DP:
# 1.overlapped sub-problems
# s = "applepenapple", wordDict = ["apple", "pen"],
# we have to repeatly find out whether apple works
# 2.the optimized sub-structure:
# The problem can be solved if we know whether applepen works
# 3. state transformation:
# dp[i] = True if dp[j] is True and s[i:j] is in wordDict
