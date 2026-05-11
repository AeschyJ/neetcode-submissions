class TimeMap:
    from collections import defaultdict
    def __init__(self):
        self.d = defaultdict(lambda: defaultdict(str))

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        def bs(d, t):
            l, r = 0, len(d) - 1
            a = -1
            while l <= r and len(d) > 0:
                m = (l + r) // 2
                if d[m] == t:
                    return m
                elif d[m] > t:
                    r = m - 1
                else:
                    a = d[m]
                    l = m + 1
            return a
        t = timestamp
        if t in self.d[key]:
            return self.d[key][timestamp]
        a = bs(list(self.d[key].keys()), t)
        return "" if a == -1 else self.d[key][a]
        
