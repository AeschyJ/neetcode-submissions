class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        from collections import deque

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n = len(grid)

        def bfs(i, row=0, col=0):
            q = deque([(0, 0)])
            visited = {(0, 0)}

            while q:
                r, c = q.popleft()
                if r == c == n - 1:
                    return True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                        if grid[nr][nc] <= i:
                            visited.add((nr, nc))
                            q.append((nr, nc))
            return False

        left = max(grid[0][0], grid[n - 1][n - 1])
        right = n * n - 1
        ans = right

        while left <= right:
            mid = (left + right) // 2
            if bfs(mid):
                ans = mid
                right = mid - 1  # 嘗試尋找更小的可行水位
            else:
                left = mid + 1  # 水位太低，必須往上加

        return ans
