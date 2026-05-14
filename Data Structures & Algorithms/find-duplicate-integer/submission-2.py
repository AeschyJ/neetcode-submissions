class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i >= 0:
            if nums[i] == 0:
                return i
            nums[i], i = 0, nums[i]
            