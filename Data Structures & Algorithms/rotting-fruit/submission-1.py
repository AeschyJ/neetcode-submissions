class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import defaultdict
        rows = len(grid)
        cols = len(grid[0])
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

        fruits = 0
        rotten = defaultdict(set)
        a = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fruits += 1
                elif grid[i][j] == 2:
                    rotten[0].add((i, j))
        def travel(fruits, time = 0):
            f = fruits
            if fruits <= 0:
                return time
            for r, c in rotten[time]:
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == 1:
                            fruits -= 1
                            rotten[time + 1].add((nr, nc))
                            grid[nr][nc] = 2
                        if fruits <= 0:
                            return time + 1  
            if f == fruits:
                return -1
            return travel(fruits, time + 1)

        return travel(fruits)