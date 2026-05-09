class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = None
        s = None
        a = 0
        for i in prices:
            if b is None:
                b = i
            elif b > i:
                b = i
                s = None
            elif s is None:
                s = i
            elif s < i:
                s = i
            if s:
                t = s - b
                a = t if t > a else a
        return a
