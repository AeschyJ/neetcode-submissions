class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from functools import reduce
        a = []
        b = nums.count(0)
        if b <= 1:
            p = reduce(lambda x, y: x * y if y else x, nums)
        for i, j in enumerate(nums):
            if b > 1:
                a.append(0)
            elif b:
                if not j:
                    a.append(p)
                else:
                    a.append(0)
            else:
                a.append(int(p/j))
        return a
