class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = set()
        x = set(i for i in nums if i in s or s.add(i))
        return list(x)[0]
            
        