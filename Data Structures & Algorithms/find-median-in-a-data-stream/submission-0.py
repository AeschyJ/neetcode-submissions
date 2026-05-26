class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.nums.sort()

    def findMedian(self) -> float:
        if len(self.nums) % 2 == 0:
            return 0.5 * (self.nums[len(self.nums)//2] + self.nums[len(self.nums)//2-1])
        else:
            return self.nums[(len(self.nums)-1)//2]