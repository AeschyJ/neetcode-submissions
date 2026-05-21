class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter, deque
        import heapq
        c = Counter(tasks)
        h = [-x for x in c.values()]
        heapq.heapify(h)
        cd = deque()
        t = 0
        while cd or h:
            t += 1
            if cd and cd[0][1] <= t:
                heapq.heappush(h, cd.popleft()[0])
            if h:
                h[0] += 1
                if h[0] < 0:
                    cd.append((h.pop(0), t + n + 1))
                else:
                    h.pop(0)
        return t