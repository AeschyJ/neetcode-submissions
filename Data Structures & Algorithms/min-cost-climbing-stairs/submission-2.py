class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = 0, 0
        for c in range(2, len(cost)+1):
            one, two = min(one + cost[c-1], two + cost[c-2]), one

        return one