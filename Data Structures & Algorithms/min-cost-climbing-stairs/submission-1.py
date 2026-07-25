class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = 0, 0
        for c in reversed(cost):
            one, two = c + min(one, two), one

        return min(one, two)