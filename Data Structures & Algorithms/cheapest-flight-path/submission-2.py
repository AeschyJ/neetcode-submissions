class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # import heapq
        from collections import defaultdict
        adj = defaultdict(list)
        for edge in flights:
            adj[edge[0]].append((edge[1], edge[2]))
        # heap = [(0, src, 0)]
        visited = set()
        self.ans = math.inf
        def dfs(node, total, stop):
            if node == dst:
                self.ans = min(self.ans, total)
                return total
            visited.add(node)
            for next_node, cost in adj[node]:
                if next_node not in visited:
                    if stop == k:
                        if next_node == dst:
                            if total + cost > self.ans:
                                continue
                            dfs(next_node, total + cost, stop + 1)
                    else:
                        if total + cost > self.ans:
                            continue
                        dfs(next_node, total + cost, stop + 1)
            visited.remove(node)
        dfs(src, 0, 0)
        return self.ans if self.ans != math.inf else -1