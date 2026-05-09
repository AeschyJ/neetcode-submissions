class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        # l = ('(',')','[',']','{','}')
        l = ('(','[','{')
        r = (')',']','}')
        d = deque()
        for i in s:
            if i in l:
                d.append(i)
            elif i in r:
                if d and d[-1] == l[r.index(i)]:
                    d.pop()
                else: return False
        if d:
            return False
        return True
            
            
        