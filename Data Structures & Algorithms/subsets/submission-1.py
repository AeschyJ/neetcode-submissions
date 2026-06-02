class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def godeep(a, idx, nums, i = 0):
            while idx[i] <= len(nums) + i - len(idx):
                if i < len(idx) - 1:
                    godeep(a, idx, nums, i + 1)
                elif i == len(idx) - 1:
                    r = []
                    for x in idx:
                        r.append(nums[x])
                    a.append(r)
                idx[i] += 1
                for x in range(len(idx[i:])):
                    idx[i+x] = idx[i] + x
                    
        n = 1
        a = [[]]
        while n <= len(nums):
            x = [i for i in range(n)]
            godeep(a, x, nums)
            n += 1
        return a
                