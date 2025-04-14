class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        hmap = defaultdict(int)
        for i in range(len(nums1)):
            for p in range(len(nums2)):
                hmap[nums1[i] + nums2[p]] += 1
        
        total = 0
        for i in range(len(nums3)):
            for p in range(len(nums4)):
                if -(nums3[i] + nums4[p]) in hmap:
                    total += hmap[-(nums3[i] + nums4[p])]
                    
        
        '''hmap = defaultdict(list)
        for i in range(len(nums2)):
            for p in range(len(nums3)):
                hmap[nums2[i] + nums3[p]].append((i, p))
        
        for i in range(len(nums1)):
            for p in range(len(nums4)):
                if -(nums1[i] + nums4[p]) in hmap:
                    for a, b in hmap[-(nums1[i] + nums4[p])]:
                        if nums1[i] + nums3[b] != -(nums2[a] + nums4[p]):
                            total += 1

        hmap = defaultdict(list)
        for i in range(len(nums1)):
            for p in range(len(nums3)):
                hmap[nums1[i] + nums3[p]].append((i, p))
        
        for i in range(len(nums2)):
            for p in range(len(nums4)):
                if -(nums2[i] + nums4[p]) in hmap:
                    for a, b in hmap[-(nums2[i] + nums4[p])]:
                        total += 1
        
        return total'''

        return total