class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        a = None
        while l <= r:
            m = (l + r) // 2
            if nums[m] >= nums[l]:
                if a is None:
                    a = nums[l]
                elif a > nums[l]:
                    a = nums[l]
                l = m + 1
            else:
                a = nums[m]
                r = m - 1
        return a
                    
        