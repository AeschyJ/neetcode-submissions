class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s = sorted(nums1 + nums2)
        if len(s) // 2 == len(s) / 2:
            return (s[len(s)//2 - 1] + s[len(s)//2]) / 2
        else:
            return s[(len(s)-1)//2]
        