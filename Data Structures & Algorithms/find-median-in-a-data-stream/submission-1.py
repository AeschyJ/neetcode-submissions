class MedianFinder:

    def __init__(self):
        self.l = []
        self.r = []

    def addNum(self, num: int) -> None:
        import heapq

        heapq.heappush(self.l, -num)
        heapq.heappush(self.r, -heapq.heappop(self.l))
        if len(self.r) > len(self.l):
            heapq.heappush(self.l, -heapq.heappop(self.r))
        

    def findMedian(self) -> float:
        if len(self.l) > len(self.r):
            return -self.l[0]
        return 0.5*(self.r[0]-self.l[0])