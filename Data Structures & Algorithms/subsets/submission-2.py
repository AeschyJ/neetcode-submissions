class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        a = [[]]
        for i in nums:
            a += [x + [i] for x in a]
        return a