class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        a = []
        sub = []
        def travel(i=0):
            if i >= len(nums):
                a.append(sub.copy())
                return
            sub.append(nums[i])
            travel(i+1)
            sub.pop()
            travel(i+1)
        travel()
        return a