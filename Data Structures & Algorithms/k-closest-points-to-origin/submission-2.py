class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        m = [[x*x + y*y, (x,y)] for x, y in points]
        s = m.sort()
        return [list(a) for d, a in m[:k]]