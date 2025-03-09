class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        hmap1 = Counter(nums1)
        hmap2 = Counter(nums2)

        res = []
        
        for key in hmap1:
            minNum = min(hmap1[key], hmap2[key])
            res += minNum * [key]

        return res