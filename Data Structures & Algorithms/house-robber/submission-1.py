class Solution:
    def rob(self, nums: List[int]) -> int:
        one, two = 0, 0
        prev = 0
        for c in nums:
            one, two = max(one - prev, two) + c, one
            prev = c
        return max(one, two)