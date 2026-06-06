class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.a = False
        path = []
        def travel(x, y, idx):
            if self.a:
                return
            if idx >= len(word):
                self.a = True
                return
            temp, board[y][x] = board[y][x], "*"
            if x > 0:
                if (x - 1, y) in path:
                    pass
                elif board[y][x - 1] == word[idx]:
                    travel(x - 1, y, idx + 1)
            if x < len(board[0]) - 1:
                if (x + 1, y) in path:
                    pass
                elif board[y][x + 1] == word[idx]:
                    travel(x + 1, y, idx + 1)
            if y > 0:
                if (x, y - 1) in path:
                    pass
                elif board[y - 1][x] == word[idx]:
                    travel(x, y - 1, idx + 1)
            if y < len(board) - 1:
                if (x, y + 1) in path:
                    pass
                elif board[y + 1][x] == word[idx]:
                    travel(x, y + 1, idx + 1)
            board[y][x] = temp
        for idx, row in enumerate(board):
            if self.a:
                break
            if word[0] in row:
                ids = [i for i, c in enumerate(row) if c == word[0]]
                for i in ids:
                    travel(i, idx, 1)
        return self.a