class Solution:
    def climbStairs(self, n: int) -> int:
        ans = 0
        for i in range(n, -1, -2):
            j = (n - i) // 2
            ans += math.comb(i + j, i)
        return ans