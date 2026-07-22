class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        import heapq
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        heap = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}
        self.ans = None
        while heap:
            level, row, col = heapq.heappop(heap)
            if row == rows - 1 and col == cols -1:
                return level
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(heap, (max(grid[nr][nc], level), nr, nc))
        