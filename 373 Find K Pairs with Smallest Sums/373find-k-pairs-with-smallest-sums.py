class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        minHeap = []
        result = []
        for i in range(min(k, len(nums1))):
            minHeap.append((nums1[i] + nums2[0], i, 0))
        
        heapify(minHeap)
        
        while k > 0 and minHeap:
            idk, first, second = heappop(minHeap)
            result.append([nums1[first], nums2[second]])
            if second + 1 < len(nums2):
                heappush(minHeap, (nums1[first] + nums2[second + 1], first, second + 1))
            k -= 1
        
        return result



        '''
        1, 1

        1, 2 - 2, 1

        1, 3 - 3, 1 - 2, 2



        '''