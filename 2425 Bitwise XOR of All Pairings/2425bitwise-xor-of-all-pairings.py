class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        bit = 0
        if len(nums1) % 2 == 0 and len(nums2) % 2 == 0:
            return bit
        elif len(nums1) % 2 == 0:
            for i in nums1:
                bit = bit ^ i
        elif len(nums2) % 2 == 0:
            for i in nums2:
                bit = bit ^ i
        else:
            for i in nums2:
                bit = bit ^ i
            for i in nums1:
                bit = bit ^ i

        return bit
