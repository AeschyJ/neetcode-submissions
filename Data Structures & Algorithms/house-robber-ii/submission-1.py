class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        first = [False] * len(nums)
        for i, c in enumerate(nums):
            if i == len(nums) - 1:
                f = [dp[i] for i in range(len(nums)-2) if first[i]]
                n = [dp[i] for i in range(len(nums)-2) if not first[i]]
                mf = max(f) if f else 0
                mn = max(n) if n else 0 
                m = max(mf-nums[0]+c, mf, mn+c)
                dp[i] = max(m, dp[i-1])
                break
            if i == 0:
                first[i] = True
                dp[i] = c
            elif i == 1:
                if dp[0] > c:
                    dp[i] = dp[0]
                    first[i] = True
                else:
                    dp[i] = c
                    first[i] = False
            else:
                if dp[i-1] > dp[i-2] + c:
                    dp[i] = dp[i-1]
                    first[i] = first[i-1]
                else:
                    dp[i] = dp[i-2] + c
                    first[i] = first[i-2]
        return dp[-1]
                