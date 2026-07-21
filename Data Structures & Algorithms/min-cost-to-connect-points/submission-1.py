class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        min_dist = [math.inf] * n
        total = 0
        min_dist[0] = 0

        while len(visited) < n:
            curr = -1
            for i in range(n):
                if i not in visited and (curr == -1 or min_dist[i] < min_dist[curr]):
                    curr = i
            visited.add(curr)
            total += min_dist[curr]

            for i in range(n):
                if i not in visited:
                    dist = abs(points[curr][0] - points[i][0]) + abs(points[curr][1] - points[i][1])
                    min_dist[i] = min(dist, min_dist[i])
        return total

            