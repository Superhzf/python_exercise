class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        row = len(matrix)
        col = len(matrix[0])
        for this_row in range(row):
            for this_col in range(col):
                val = matrix[this_row][this_col]
                if not (this_row == 0 or this_col == 0 or matrix[this_row-1][this_col-1] == val):
                    return False
        return True

# Iterate each element of the element, if it not the top-left element of ths diagonal
# It should be equal to it's previous element
