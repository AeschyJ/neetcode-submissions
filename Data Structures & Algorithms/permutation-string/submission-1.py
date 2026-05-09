class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import defaultdict
        d = defaultdict(int)
        for i in s1:
            d[i] += 1
        l = s2[0]
        for r in range(len(s2)):   
            if r >= len(s1):
                d[l] += 1
                l = s2[r-len(s1)+1]
                d[s2[r]] -= 1
            else:
                d[s2[r]] -= 1
            if max(d.values()) == 0:
                return True
        return False