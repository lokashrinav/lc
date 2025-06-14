class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums3 = set(nums2)
        nums4 = set(nums1)
        count1 = count2 = 0
        for i in range(len(nums1)):
            if nums1[i] in nums3:
                count1 += 1

        for i in range(len(nums2)):
            if nums2[i] in nums4:
                count2 += 1
        
        return [count1, count2]