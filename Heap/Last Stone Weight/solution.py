# Overall time complexity is O(nlog(n))
import heapq as h
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]*=-1
        heapq.heapify(stones) # O(n)
        while len(stones)>1:
            a = h.heappop(stones) # O(log(n))
            b = h.heappop(stones)
            if a!=b:
                h.heappush(stones, a-b) # O(log(n))
        return abs(stones[0]) if stones else 0
