# DP solution
# dp(i): all unique combinations whose sum is i.
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        dp = [None] * (target+1)
        dp[0] = []
        for c in candidates:
            for i in range(c, target + 1):
                if dp[i-c] != None:
                    if dp[i] == None:
                        # Initialize
                        dp[i] = []
                    if i == c:
                        # This will happen only when i == c
                        dp[i].append([c])
                    else:
                        for l in dp[i-c]:
                            dp[i].append(l+[c])
        return dp[target]


# Backtracking solution
def combinationSumBT(candidates: List[int], target: int) -> List[List[int]]:
    def backtrack(cans, remain, path):
        for i, can in enumerate(cans):
            if remain - can == 0:
                solutions.append(path+[can])
            elif remain - can > 0:
                backtrack(cans[i:], remain-can, path+[can])

    solutions=[]
    backtrack(candidates, target, [])
    return solutions

# This problem can be solved by either DP or backtracking
#
