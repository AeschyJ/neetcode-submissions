class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from functools import reduce
        a = []
        b = nums.count(0)
        if b <= 1:
            p = reduce(lambda x, y: x * y if y else x, nums)
        for i, j in enumerate(nums):
            if b > 1 or (b and j):
                a.append(0)
            elif b:
                a.append(p)
            else:
                a.append(p // j)
        return a
