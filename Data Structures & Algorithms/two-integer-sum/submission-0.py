class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, j in enumerate(nums):
            a = target - j
            if a in d:
                return [d[a], i]
            else:
                d[j] = i