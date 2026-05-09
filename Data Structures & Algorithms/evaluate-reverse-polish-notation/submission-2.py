class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        from collections import deque
        from functools import reduce
        import math
        d = deque()
        o = ('+','-','*','/')
        for i in tokens:
            if i not in o:
                d.appendleft(int(i))
            else:
                if i == '+':
                    d[1] += d[0]
                    d.popleft()
                elif i == '-':
                    d[1] -= d[0]
                    d.popleft()
                elif i == '*':
                    d[1] *= d[0]
                    d.popleft()
                else:
                    d[1] = int(d[1] / d[0])
                    d.popleft()
        return d[0]
        