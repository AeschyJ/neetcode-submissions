class TimeMap:
    from collections import defaultdict
    def __init__(self):
        self.d = defaultdict(lambda: defaultdict(str))

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        t = timestamp
        while t > 0:
            if t in self.d[key]:
                return self.d[key][t]
            t -= 1
        return ""
        
