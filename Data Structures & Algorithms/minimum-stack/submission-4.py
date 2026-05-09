class MinStack:

    def __init__(self):
        from collections import deque
        self.m = deque()
        self.mini = 0
        self.t = deque()

    def push(self, val: int) -> None:
        if not self.m or val < self.m[-1]:
            self.mini = val
        self.m.append(self.mini)
        self.t.append(val)


    def pop(self) -> None:
        if self.m[-1] == self.mini:
            if len(self.m) > 1: self.mini = self.m[-2]
            else: self.mini = None
        self.t.pop()
        self.m.pop()

    def top(self) -> int:
        return self.t[-1]

    def getMin(self) -> int:
        return self.m[-1]
