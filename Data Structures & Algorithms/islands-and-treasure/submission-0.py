class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def travel(r, c, distance = 0):
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] <= 0 or grid[nr][nc] <= distance + 1:
                        continue
                    else:
                        grid[nr][nc] = distance + 1
                        travel(nr, nc, grid[nr][nc])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    travel(r, c)