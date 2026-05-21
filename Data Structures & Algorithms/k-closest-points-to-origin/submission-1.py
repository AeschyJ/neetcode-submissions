class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        m = [[x**2 + y**2, [x,y]] for x, y in points]
        s = m.sort()
        return [a for d, a in m[:k]]