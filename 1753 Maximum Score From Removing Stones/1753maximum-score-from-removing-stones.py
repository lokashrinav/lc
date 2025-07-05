class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:

        minHeap = [-a, -b, -c]
        heapify(minHeap)
        total = 0
        
        while len(minHeap) > 1:
            out1 = -heappop(minHeap)
            out2 = -heappop(minHeap)
            total += 1

            out1 -= 1
            out2 -= 1
            if out1:
                heappush(minHeap, -out1)

            if out2:
                heappush(minHeap, -out2)

        return total
        
            
            
            
        
        