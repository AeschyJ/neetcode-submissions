class LRUCache:

    def __init__(self, capacity: int):
        from collections import defaultdict
        self.capacity = capacity
        self.oper = 0
        self.cache = defaultdict(int)
        self.value = defaultdict(int)

    def get(self, key: int) -> int:
        if key in self.value:
            self.cache[key], self.oper = self.oper, self.oper + 1
            return self.value[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            pass
        elif len(self.value) >= self.capacity:
            m = min(self.cache, key = self.cache.get)
            self.cache.pop(m)
            self.value.pop(m)
        self.cache[key], self.value[key], self.oper = self.oper, value, self.oper + 1
