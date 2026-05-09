class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        a=[]
        for i in range(len(nums)-k+1):
            a.append(max(nums[i:i+k]))
        return a
        