class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        from collections import defaultdict
        d = defaultdict(int)
        for i, j in enumerate(numbers):
            if target - j in d:
                return [d[target - j], i + 1]
            d[j] = i + 1