class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        a = []
        def travel(arr, nums, target, curridx):
            for idx, n in enumerate(nums):
                if idx < curridx:
                    continue
                elif target < n:
                    continue
                elif target == n:
                    arr.append(n)
                    a.append(arr.copy())
                    arr.pop()
                else:
                    arr.append(n)
                    travel(arr, nums, target - n, idx)
                    arr.pop()
        travel([], nums, target, 0)
        return a