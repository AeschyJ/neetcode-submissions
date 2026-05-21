class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        l = [[a, i, 0] for a, i in list(Counter(tasks).items())]
        t = 0
        while l:
            t += 1
            l.sort(key = lambda x: (0 if x[2] <= t else 1, -x[1]))
            if l[0][1] == 0:
                break
            if l[0][2] > t:
                ...
            else:
                l[0][1] -= 1
                if l[0][1] == 0:
                    l[0][2] = math.inf
                else: l[0][2] = t + n + 1
        return t - 1
