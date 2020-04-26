class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board
        self.word = word

        for row in range(self.ROWS):
            for col in range(self.COLS):
                is_valid = self.backtrack(row, col, 0)
                if is_valid:
                    return True

        return False

    def backtrack(self, row, col, idx):
        if idx == len(self.word):
            return True

        if row < 0 or row == self.ROWS or col < 0 or col == self.COLS or self.board[row][col] != self.word[idx]:
            return False

        self.board[row][col] = '#'
        for row_offset, col_offset in [(0,1), (1,0), (0,-1), (-1,0)]:
            ret = self.backtrack(row+row_offset, col+col_offset, idx+1)
            if ret:
                return True

        self.board[row][col] = self.word[idx]
        return False
