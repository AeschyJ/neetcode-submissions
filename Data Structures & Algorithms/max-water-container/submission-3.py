class Solution:
    def maxArea(self, heights: List[int]) -> int:
        a = 0
        le = len(heights) - 1
        l, r = 0, le
        while l < r:
            a = min(heights[l], heights[r]) * le if min(heights[l], heights[r]) * le > a else a
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            le -= 1
        return a
                
        