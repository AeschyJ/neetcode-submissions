class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        h = set(heights)
        a = 0
        for i in sorted(h):
            x = 0
            for ind in range(len(heights)):
                if heights[ind] >= i:
                    x += i
                    # print("Big", i, heights[ind], x)
                    if ind == len(heights) - 1:
                        a = x if a < x else a
                else:
                    a = x if a < x else a
                    x = 0
                    # print("low", i, heights[ind], a)
        return a
                
        