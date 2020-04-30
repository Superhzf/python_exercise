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
def combinationSumBT(self, candidates: List[int], target: int) -> List[List[int]]:
    def backtrack(cans, target, path):
        for idx, can in enumerate(cans):
            if target - can == 0:
                output.append(path + [can])
                break
            elif target - can > 0:
                backtrack(cans[idx:], target - can, path+[can])

    output = []
    candidates = sorted(candidates)
    backtrack(candidates, target, [])
    return output
# This problem can be solved by either DP or backtracking
#
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(c_list, target, subset):
            for idx, c in enumerate(c_list):
                if target - c == 0:
                    # we cannt do subset.append(c) here
                    # because subset is an object, if we do subset.pop()
                    # output will be affected
                    output.append(subset+[c])
                    break
                elif target - c > 0:
                    subset.append(c)
                    backtrack(c_list[idx:], target - c, subset)
                    # If we append c to subset, then we have to pop out the last element
                    subset.pop()

        output = []
        candidates = sorted(candidates)
        backtrack(candidates, target, [])
        return output
