class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        a = []
        candidates.sort()
        def travel(arr, nums, target, idx):
            for i, n in enumerate(nums):
                if i <= idx:
                    continue 
                elif target < n:
                    return
                elif i > idx + 1 and nums[i-1] == n:
                    continue
                elif target == n:
                    arr.append(n)
                    a.append(arr.copy())
                    arr.pop()
                else:
                    arr.append(n)
                    # print(arr, target - n, i)
                    travel(arr, nums, target - n, i)
                    arr.pop()
        travel([], candidates, target, -1)
        return a