class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict
        a, c = 0, 0
        d = defaultdict(int)
        for i, j in enumerate(s):
            if j in d:
                a = c if a < c else a
                d = {k: v for k, v in d.items() if v > d[j]}
                d[j] = i
                c = len(d)
            elif i == len(s) - 1:
                a = c + 1 if a < c + 1 else a
            else:
                c += 1
                d[j] = i
        return a
        