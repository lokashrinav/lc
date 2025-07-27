class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        if sum(nums2) + nums2.count(0) == sum(nums1) + nums1.count(0):
            return sum(nums2) + nums2.count(0)

        if sum(nums2) + nums2.count(0) < sum(nums1) + nums1.count(0):
            nums1, nums2 = nums2, nums1
        
        
        
        if nums1.count(0) == 0:
            return -1
        
        return sum(nums2) + nums2.count(0)