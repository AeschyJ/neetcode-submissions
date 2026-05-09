class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lh , rh = 0, 0
        a = 0
        while l < r:
            if height[l] >= lh:
                lh = height[l]
            if height[r] >= rh:
                rh = height[r]
            if lh <= rh:
                l += 1
                a += max(lh - height[l], 0)
            else:
                r -= 1
                a += max(rh - height[r], 0)
        return a
