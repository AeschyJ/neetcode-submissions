class Solution:
    def climbStairs(self, n: int) -> int:
        fib1, fib2 = 1, 1
        for _ in range(n - 1):
            fib1, fib2 = fib1 + fib2, fib1
        return fib1