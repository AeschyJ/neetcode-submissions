class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        from collections import defaultdict
        board = [['#' for _ in range(n)] for _ in range(n)]
        d = defaultdict(list)
        a = []
        def switch(x ,y , back = False):
            if x >= n or y >= n or x < 0 or y < 0:
                return
            if back:
                for x1, y1 in d[(x, y)]:
                    board[x1][y1] = '#'
                d[(x, y)].clear()
            else:
                for i in range(n):
                    if board[x][i] == '#':
                        board[x][i] = '.'
                        d[(x, y)].append((x, i))
                for i in range(n):
                    if board[i][y] == '#':
                        board[i][y] = '.'
                        d[(x, y)].append((i, y))
                for i in range(1, n):
                    x1, y1 = x - i, y - i
                    if x1 >= 0 and y1 >= 0:
                        if board[x1][y1] == '#':
                            board[x1][y1] = '.'
                            d[(x, y)].append((x1, y1))
                    x1, y1 = x - i, y + i
                    if x1 >= 0 and y1 < n:
                        if board[x1][y1] == '#':
                            board[x1][y1] = '.'
                            d[(x, y)].append((x1, y1))
                    x1, y1 = x + i, y + i
                    if x1 < n and y1 < n:
                        if board[x1][y1] == '#':
                            board[x1][y1] = '.'
                            d[(x, y)].append((x1, y1))
                    x1, y1 = x + i, y - i
                    if x1 < n and y1 >= 0:
                        if board[x1][y1] == '#':
                            board[x1][y1] = '.'
                            d[(x, y)].append((x1, y1))
        def backtrack(idx = 0):
            if idx >= n:
                a.append(["".join(x) for x in board])
                return
            for i, c in enumerate(board[idx]):
                if c == '#':
                    board[idx][i] = 'Q'
                    switch(idx, i)
                    backtrack(idx + 1)
                    switch(idx, i, True)
                    board[idx][i] = '#'
        backtrack()
        return a