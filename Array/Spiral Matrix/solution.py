class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == []:
            return None
        row = len(matrix)
        col = len(matrix[0])

        seen = [[False] * col for _ in range(row)]
        res = []
        direct_r = [0,1,0,-1]
        direct_c = [1,0,-1,0]
        r = 0
        c = 0
        di = 0

        for _ in range(row*col):
            res.append(matrix[r][c])
            seen[r][c] = True
            cr = r + direct_r[di] # candidate row
            cc = c + direct_c[di] # candidate col
            if cr >= 0 and cr < row and cc >= 0 and cc < col and seen[cr][cc] is False:
                r = cr
                c = cc
            else:
                di = (di+1) % 4
                r = r + direct_r[di]
                c = c + direct_c[di]
        return res

# Just simulate the whole procedure
