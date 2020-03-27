class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x:x[0])
        size = len(intervals)
        for idx in range(size - 1):
            if intervals[idx] != 'delete':
                if intervals[idx][1] >= intervals[idx+1][0]:
                    if intervals[idx+1][1] > intervals[idx][1]:
                        intervals[idx+1] = [intervals[idx][0],intervals[idx+1][1]]
                        intervals[idx] = 'delete'
                    else:
                        intervals[idx+1] = 'delete'
                        intervals[idx+1],intervals[idx] = intervals[idx], intervals[idx+1]

        return [k for k in intervals if k != 'delete']

# I solved this problem myself
# Step 1: sort the intervals based on the left side
# Step 2: compare intervals with it's next one, if right side interval[idx] >=
# the left side of interval[idx+1], then combine them, 'delete' is used as the
# place holder to make sure the idx is correct
