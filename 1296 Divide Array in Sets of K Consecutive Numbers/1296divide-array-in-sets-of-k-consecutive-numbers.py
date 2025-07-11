class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:

        hmap = Counter(nums)
        minHeap = list(set(nums))
        heapify(minHeap)

        if len(nums) % k:
            return False
        
        while minHeap:
            out = minHeap[0]
            for i in range(out, out + k):
                if i not in hmap or hmap[i] == 0:
                    return False
                hmap[i] -= 1
                        
            while minHeap and hmap[minHeap[0]] == 0:
                heappop(minHeap)
            #print(hmap)
            
        return True