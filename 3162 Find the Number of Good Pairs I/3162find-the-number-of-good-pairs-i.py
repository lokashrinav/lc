class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        total = 0
        hset = set()
        for i in range(len(nums1)):
            for p in range(len(nums2)):
                if nums1[i] % (nums2[p] * k) == 0:
                    hset.add((i, p))
        
        return len(hset)