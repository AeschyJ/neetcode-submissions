class Solution:
    def maxArea(self, heights: List[int]) -> int:
        a = 0
        for in1, i in enumerate(heights[:-1]):
            for in2, j in enumerate(heights[in1+1:]):
                a = (in2 + 1) * min(i, j) if (in2 + 1) * min(i, j) > a else a
                # print(in1, in2+1, min(i,j), a)
        return a
        