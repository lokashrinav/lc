2702. Minimum Operations to Make Numbers Non-positiveclass Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) < len(nums2):
            nums2, nums1 = nums1, nums2

        l, r = 0, len(nums1)

        '''

        2, 3, 7
        4, 5

        i + 1

        i = 0 -> j - 1
        i = 1 -> 

        '''

        while l <= r:
            m = (l + r) // 2
            j = (len(nums2) + len(nums1) + 1) // 2 - i
            if nums1 and nums2 and nums1[i] > nums2[j + 1]:
                r = m - 1
            elif nums1 and nums2 and nums2[j] > nums1[i + 1]:
                l = m + 1
            elif nums1 and nums2 and nums1[i + 1] >= nums2[j] and nums2[j + 1] >= nums1[i]:
                med = 
                return med






