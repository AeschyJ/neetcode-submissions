class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq
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
            tlist = [t for t in times if t[0] == dest]
            for t in tlist:
                heapq.heappush(hp, (t[2] + time, t[1]))
        return time if len(path) == n else -1