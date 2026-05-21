class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        t = k - 1
        def quick(l, r):
            import random
            p = random.randint(l, r)
            nums[p], nums[r] = nums[r], nums[p]
            idx = l
            for i in range(l, r):
                if nums[i] > nums[r]:
                    nums[idx], nums[i] = nums[i], nums[idx]
                    idx += 1
            nums[idx], nums[r] = nums[r], nums[idx]
            if idx == t:
                return nums[idx]
            elif idx > t:
                return quick(l, idx - 1)
            else:
                return quick(idx + 1, r)
        return quick(0, len(nums) - 1)