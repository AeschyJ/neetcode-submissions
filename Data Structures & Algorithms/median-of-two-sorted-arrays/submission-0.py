class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = nums1 + nums2
        s = sorted(n)
        print(s, len(s)//2, len(s) / 2)
        if len(s) // 2 == len(s) / 2:
            return (s[len(s)//2 - 1] + s[len(s)//2]) / 2
        else:
            return s[(len(s)-1)//2]
        