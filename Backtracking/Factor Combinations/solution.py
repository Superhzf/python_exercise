class Solution:
    def getFactors(self, n: int) -> List[List[int]]:

        def backtrack(target, subset, start):
            # The reason to have subset parameter is to find the factor of target
            # for example, when target = 12, start = 2, the next target = 12/2=6
            # we only have to keep 2 and find factor of 6
            while start * start <= target:
                if target % start == 0:
                    results.append(subset + [start, target // start])
                    backtrack(target // start, subset + [start], start)
                start += 1

        results = []
        backtrack(n, [], 2)
        return results
