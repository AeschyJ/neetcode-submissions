class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        a = 0
        if h >= sum(piles):
            return l
        elif h == len(piles):
            return r
        while l <= r:
            m = (l + r) // 2
            t = sum((v + m - 1) // m for v in piles)
            if t > h:
                l = m + 1
            else:
                a = m
                r = m - 1
        return a
        