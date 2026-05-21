class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        return heapq.nsmallest(k, points, key = lambda d: d[0] ** 2 + d[1] ** 2)