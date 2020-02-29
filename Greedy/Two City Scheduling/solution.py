# (Time, Space) Complexity : O(nlog(n)), O(n)

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # Key Point:
        #   Compare fees between multiple people is nonsense
        #   The key point is fee difference between two country for a man
        # Strategy:
        #   1. Count the diff for each person and sort all people with it
        #      By doning this, we can find who prefer A or B is better choice
        #   2. divide people into two, one for country A and another for B
        #   3. sum their fee
        half = len(costs)//2
        costs.sort(key=lambda x: x[0] - x[1]) # This is the key
        return sum(list(zip(*costs[:half]))[0]) + sum(list(zip(*costs[half:]))[1])
