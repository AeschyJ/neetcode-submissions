class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq
        from collections import defaultdict
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        hp = []
        path = set()
        heapq.heappush(hp, (0, k))
        time = 0
        while hp:
            delay, dest = heapq.heappop(hp)
            if dest in path:
                continue
            time = delay
            path.add(dest)

            for nextnode, spend in graph[dest]:
                if nextnode not in path: 
                    heapq.heappush(hp, (time + spend, nextnode))

        return time if len(path) == n else -1