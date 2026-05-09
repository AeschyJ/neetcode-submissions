class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        a, l, r = 1, 0, 0
        d = defaultdict(int)
        d[s[l]] += 1
        m = s[l]
        t = 1
        while r < len(s) - 1:
            r += 1
            t += 1
            d[s[r]] += 1
            if d[s[r]] > d[m]:
                m = s[r]
            if t > d[m] + k:
                d[s[l]] -= 1
                if s[l] == m:
                    m = next((k for k, v in d.items() if v >= d[m]), None)
                t -= 1
                l += 1
            else:
                a = t if t > a else a
        return a