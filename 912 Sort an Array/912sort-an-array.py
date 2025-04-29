class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        l, r = 0, len(nums) - 1

        def mergeSort(l, r):
            if l == r:
                return [nums[l]]
            if l > r:
                return []

            m = (l + r) // 2
            left = mergeSort(l, m)
            right = mergeSort(m + 1, r)
            return merge(left, right)

        def merge(nums1, nums2):
            res = []
            i, j = 0, 0
            while i < len(nums1) or j < len(nums2):
                first, second = float('inf'), float('inf')
                if i < len(nums1):
                    first = nums1[i]
                if j < len(nums2):
                    second = nums2[j]
                
                if first < second:
                    res.append(first)
                    i += 1
                else:
                    res.append(second)
                    j += 1
            return res

        
        return mergeSort(l, r)