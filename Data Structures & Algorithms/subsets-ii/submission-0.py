class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        a = []
        arr = []
        nums.sort()
        def travel(i, prev, idx):
            if i >= len(nums):
                a.append(arr.copy())
                return
            elif i > idx + 1 and nums[i] == prev:
                pass
            else:
                arr.append(nums[i])
                travel(i + 1, nums[i], i)
                arr.pop()
            travel(i + 1, nums[i], idx)
        travel(0, None, -1)
        return a