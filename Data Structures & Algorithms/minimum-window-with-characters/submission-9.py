class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        d = defaultdict(int)
        for i in t:
            d[i] += 1
        l = 0
        a = ""
        for r in range(len(s)):
            if s[r] in d:
                d[s[r]] -= 1
            while max(d.values()) <= 0:
                # print("done",l,r,dict(d), s[l:r+1])
                if len(a) > r - l + 1 or not a:
                    a = s[l:r+1]
                if s[l] in d:
                    d[s[l]] += 1
                if l < r:
                    l += 1
            while s[l] not in d and l < r:
                l += 1
        return a
        