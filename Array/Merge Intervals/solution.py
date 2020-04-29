class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        size = len(intervals)
        i = 0
        while i < size - 1:
            if intervals[i][1] >= intervals[i+1][1]:
                intervals.pop(i+1)
                size -= 1
                continue
            elif intervals[i][1] >= intervals[i+1][0]:
                intervals[i] = [intervals[i][0],intervals[i+1][1]]
                intervals.pop(i+1)
                size -= 1
                continue
            i += 1
        return intervals



# I solved this problem myself
# Step 1: sort the intervals based on the left side
# Step 2: compare intervals with it's next one, if right side interval[idx] >=
# the left side of interval[idx+1], then combine them,
