class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        a=[]
        q = deque()
        for i, j in enumerate(nums):
            if q and q[0] < i-k+1:
                q.popleft()
            while q and nums[q[-1]] < j:
                q.pop()
            q.append(i)
            if i >= k-1:
                a.append(nums[q[0]])
        return a
        