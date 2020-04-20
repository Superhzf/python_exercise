# prolblem description:
# https://leetcode.com/problems/n-queens/solution/
# rule: no two queens share the same row, column, or diagonal
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def could_place(row,col):
            return (cols[col] + major_diag[row-col] + minor_diag[row+col]) == 0

        def place_queen(row,col):
            queens.add((row,col))
            cols[col] = 1
            major_diag[row-col] = 1
            minor_diag[row+col] = 1

        def remove_queen(row,col):
            queens.remove((row,col))
            cols[col] = 0
            major_diag[row-col] = 0
            minor_diag[row+col] = 0

        def add_solution():
            solution = []
            for _, col in sorted(queens):
                solution.append('.' * col + 'Q' + '.' * (n - col - 1))
            output.append(solution)

        def backtrack(row = 0):
            for col in range(n):
                if could_place(row,col):
                    place_queen(row, col)
                    if row + 1 == n:
                        add_solution()
                    else:
                        backtrack(row+1)
                    remove_queen(row,col)

        cols = [0] * n
        major_diag = [0] * (2*n-1)
        minor_diag = [0] * (2*n-1)
        queens = set()
        output = []
        backtrack()
        return output
