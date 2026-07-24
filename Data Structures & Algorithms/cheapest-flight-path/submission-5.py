class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        from collections import deque, defaultdict
        adj = defaultdict(list)
        for edge in flights:
            adj[edge[0]].append((edge[1], edge[2]))
        heap = deque()
        heap.append([src, 0, 0])
        self.ans = math.inf
        node_min = [math.inf] * n
        while heap:
            dest, total, stop = heap.popleft()
            if stop > k:
                break
            for nxt, cost in adj[dest]:
                if total + cost >= node_min[nxt]:
                    continue
                node_min[nxt] = total + cost
                if nxt == dst:
                    self.ans = total + cost
                else:
                    heap.append([nxt, total + cost, stop + 1])
        return self.ans if self.ans != math.inf else -1