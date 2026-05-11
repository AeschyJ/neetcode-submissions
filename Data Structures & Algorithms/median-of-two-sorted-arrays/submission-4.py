class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getinf(i, l):
            if i < 0:
                return -math.inf
            elif i == len(l):
                return math.inf
            else:
                return l[i]

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m1, m2 = len(nums1), len(nums2)
        l, r = 0, m1
        while l <= r:
            i = (l + r) // 2
            j = ((m1 + m2 + 1) // 2) - i
            # print('i',i,'j',j,'l1',getinf(i-1,nums1),'r2',getinf(j,nums2),
            # 'r1',getinf(j-1,nums2),'l2',getinf(i,nums1))
            if getinf(i-1, nums1) <= getinf(j, nums2) and getinf(j-1,nums2) <= getinf(i,nums1):
                if (m1 + m2) // 2 != (m1 + m2) / 2:
                    return max(getinf(i-1,nums1), getinf(j-1, nums2))
                else: return (max(getinf(i-1,nums1), getinf(j-1, nums2)) + min((getinf(i,nums1), getinf(j, nums2)))) / 2
            elif getinf(i-1,nums1) > getinf(j,nums2):
                r = i - 1
            else:
                l = i + 1
                    
                    
        