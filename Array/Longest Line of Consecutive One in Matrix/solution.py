class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        total_count = 0
        neighbor_list = [(0,1), (1,0), (1,1), (1,-1)]
        seen = [set(), set(), set(), set()]
        if M == []:
            return total_count
        if M == [[]]:
            return total_count
        row = len(M)
        col = len(M[0])

        for this_row in range(row):
            for this_col in range(col):
                this_ele = M[this_row][this_col]
                if this_ele == 1:
                    for idx, this_neighbor in enumerate(neighbor_list):
                        if (this_row,this_col) not in seen[idx]:
                            seen[idx].add((this_row,this_col))
                            this_count = 1
                            cr = this_row + this_neighbor[0]
                            cc = this_col + this_neighbor[1]
                            while cr >= 0 and cr < row and cc >= 0 and cc < col and M[cr][cc] == 1:
                                seen[idx].add((cr,cc))
                                this_count += 1
                                cr += this_neighbor[0]
                                cc += this_neighbor[1]
                            total_count = max(total_count,this_count)
        return total_count

# I figure out this problem myself
# Note:
# We do not need to traversal all 8 dictions.
# use "seen" to avoid unnecessary visit
