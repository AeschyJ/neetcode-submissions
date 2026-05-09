class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        from collections import defaultdict
        d = defaultdict(bool)
        for i in nums:
            d[i] = True
        s = sorted(d)
        a = 0
        b = 1
        for i in range(len(s)):
            if i + 1 < len(s):
                b = b + 1 if s[i+1] == s[i] + 1 else 1
            if b > a:
                a = b
        return a
        