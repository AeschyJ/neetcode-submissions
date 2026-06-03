class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        a = []
        nums.sort()
        def travel(arr, nums, target, curridx):
            for idx, n in enumerate(nums[curridx:]):
                if target < n:
                    return
                if target == n:
                    a.append(arr + [n])
                travel(arr + [n], nums, target - n, curridx + idx)
        travel([], nums, target, 0)
        return a