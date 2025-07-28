class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        maxHeap, minHeap = self.maxHeap, self.minHeap
        if not minHeap or num < minHeap[0]:
            heappush(maxHeap, -num)
        else:
            heappush(minHeap, num)
        
        while len(maxHeap) < len(minHeap):
            out = heappop(minHeap)
            heappush(maxHeap, -out)
        
        while len(maxHeap) - len(minHeap) > 1:
            out = -heappop(maxHeap)
            heappush(minHeap, out)

    def findMedian(self) -> float:
        #print(self.maxHeap, self.minHeap)
        maxHeap, minHeap = self.maxHeap, self.minHeap
        if len(maxHeap) > len(minHeap):
            return -maxHeap[0]
        else:
            return (-maxHeap[0] + minHeap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()