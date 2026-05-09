class Solution:
    def search(self, nums: List[int], target: int) -> int:
        from collections import deque
        p = (len(nums) - 1) // 2
        d = deque()
        d.append(0)
        d.append(len(nums)-1)
        if target == nums[0] or target == nums[-1]:
            return nums.index(target)
        while 0 <= p < len(nums):
            if nums[p] > target:
                if d[-1] != p:
                    d.append(p)
                    p = (d[0] + p) // 2
                else: return -1
            elif nums[p] < target:
                if d[0] != p:
                    d.appendleft(p)
                    p = (d[-1] + p) // 2
                else: return -1
            else:
                return p
        