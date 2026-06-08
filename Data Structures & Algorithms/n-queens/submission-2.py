class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        a = []
        cols = set()
        diag_pos = set()
        diag_neg = set()
        queens = [-1] * n
        def backtrack(x = 0):
            if x >= n:
                board = ['.' * x + 'Q' + '.' * (n - x - 1) for x in queens]
                a.append(board)
                return
            for y in range(n):
                if y in cols or (x + y) in diag_pos or (x - y) in diag_neg:
                    continue
                cols.add(y)
                diag_pos.add(x + y)
                diag_neg.add(x - y)
                queens[x] = y
                backtrack(x + 1)
                cols.remove(y)
                diag_pos.remove(x + y)
                diag_neg.remove(x - y)
        backtrack()
        return a