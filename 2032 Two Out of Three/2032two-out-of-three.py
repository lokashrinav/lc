class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        
        def func(nums1, nums2):
            set1 = set(nums1)
            set2 = set(nums2)

            final = []

            for elem in nums1:
                if elem in nums2:
                    final.append(elem)
            
            return set(final)

        set1 = func(nums1, nums2)
        set2 = func(nums2, nums3)
        set3 = func(nums1, nums3)

        set1.update(set2)
        set1.update(set3)

        return list(set1)