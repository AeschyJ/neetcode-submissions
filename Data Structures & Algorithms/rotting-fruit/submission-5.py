class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

        fruits = 0
        stack = [[]]
        time = -1
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fruits += 1
                elif grid[i][j] == 2:
                    stack[0].append((i, j))
        while stack:
            rottens = stack.pop()
            for r, c in rottens:
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            fruits -= 1
                            if not stack:
                                stack.append([])
                            stack[0].append((nr, nc))
            time += 1
        return time if fruits == 0 else -1