class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        dt = {}
        for i in nums:
            if i not in dt:
                dt[i] = 1
            else:
                dt[i] += 1
        ans = 0
        for j in nums:
            if k == 0:
                if j in dt and dt[j] > 1:
                    ans += 1
                    del dt[j] # delete all of them because the pair should be unique
            else:
                if j-k in dt: # here is j-k only instead of k-j because we will meet k-j later
                    ans += 1
                    del dt[j-k]
        return ans

# hashtable
# Using two pointers will exceed time
