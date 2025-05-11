class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        '''

        1 + 3 = 4
        5 + 4 = 9
        9 + 8 = 17
        '''

        minHeap = sticks

        heapify(minHeap)

        total = 0

        while len(minHeap) > 1:
            out1 = heappop(minHeap)
            out2 = heappop(minHeap)
            total += out1 + out2
            heappush(minHeap, out1 + out2)
        
        return total

        