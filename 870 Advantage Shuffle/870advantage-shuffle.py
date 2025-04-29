class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:

        '''
        2, 7, 11, 15
        1, 4, 10, 11
        '''
        nums1.sort()
        hmap = [(nums2[i], i) for i in range(len(nums2))]
        hmap.sort()

        queue = deque(nums1)
        res = [0] * len(nums2)

        for i in range(len(nums2) - 1, -1, -1):
            idk = hmap[i][0] 
            if idk >= queue[-1]:
                res[hmap[i][1]] = queue.popleft()
            else:
                res[hmap[i][1]] = queue.pop()
        
        return res