class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        d = defaultdict(int)
        l = 0
        m = 1
        for r in range(len(s)):
            d[s[r]] += 1
            m = max(m, d[s[r]])
            if r - l + 1 > m + k:
                d[s[l]] -= 1
                l += 1
        return len(s) - l