class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        row, col = len(grid), len(grid[0])
        self.a = 0
        def travel(r, c, area = 1):
            if area > self.a:
                self.a = area
            grid[r][c] = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col:
                    if grid[nr][nc] == 1:
                        area = travel(nr, nc, area + 1)
            return area
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    travel(r, c, 1)
        return self.a