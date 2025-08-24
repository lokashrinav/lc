class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        
        '''
        1, 2, 
        '''

        hmap = Counter(barcodes)

        minHeap = [(-val, key) for key, val in hmap.items()]

        heapify(minHeap)
        res = []

        while len(minHeap) >= 2:
            out1 = heappop(minHeap)
            out2 = heappop(minHeap)
            
            res.append(out1[1])
            res.append(out2[1])

            if out1[0] + 1 != 0:
                heappush(minHeap, (out1[0] + 1, out1[1]))
            if out2[0] + 1 != 0:
                heappush(minHeap, (out2[0] + 1, out2[1]))
        
        if minHeap:
            out1 = heappop(minHeap)
            res.append(out1[1])
        
        return res
        


