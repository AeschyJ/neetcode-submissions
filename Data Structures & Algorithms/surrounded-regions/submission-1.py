class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        e = set()
        def edge(r, c):
            e.add((r, c))
            board[r][c] = "X"
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if board[nr][nc] == "O":
                        edge(nr, nc)

        for i in range(rows):
            if board[i][0] == "O":
                edge(i, 0)
            if board[i][cols - 1] == "O":
                edge(i, cols - 1)
        for i in range(cols):
            if board[0][i] == "O":
                edge(0, i)
            if board[rows - 1][i] == "O":
                edge(rows - 1, i)
        for i in range(rows):
            for j in range(cols):
                if (i, j) in e:
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
            