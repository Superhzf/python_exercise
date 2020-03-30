import itertools
class Solution(object):
    def maxDistToClosest(self, seats):
        ans = 0
        for seat, group in itertools.groupby(seats):
            if seat == 0:
                K = len(list(group))
                ans = max(ans, (K+1)//2)

        return max(ans, seats.index(1), seats[::-1].index(1))

# The idea is to group  seats by 0 and 1,
# then, suppose there are K zeros between two 1s, then the max distance
# would be k+1/2. The edge case is that the left(right) most elements are zeros
