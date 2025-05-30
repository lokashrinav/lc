class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        hmap = {}
        for i in range(len(nums1)):
            hmap[nums2[i]] = i

        res = [0] * len(nums1)

        for i, elem in enumerate(nums1):
            res[i] = hmap[elem]
        
        return res

