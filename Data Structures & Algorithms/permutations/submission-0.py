class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        a = []
        d = {x:1 for x in nums}
        def per(arr):
            for x in [x[0] for x in d.items() if x[1] > 0]:
                d[x] = 0
                arr.append(x)
                if len(arr) == len(nums):
                    a.append(arr.copy())
                per(arr)
                arr.pop()
                d[x] = 1
        per([])
        return a