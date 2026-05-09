class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        from collections import defaultdict
        d = defaultdict(list)
        sort = reversed(sorted(zip(position, speed)))
        p, s = zip(*sort)
        print(p,s)
        for i in range(len(p)):
            if not d:
                d[(target - p[i]) / s[i]].append(i)
            elif (target - p[i]) / s[i] < max(d.keys()):
                d[max(d.keys())].append(i)
            else:
                d[(target - p[i]) / s[i]].append(i)
        return len(d)
        