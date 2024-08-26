class MedianFinder:

    def __init__(self):
        self.lis = []
        self.lis2 = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.lis, -num)
        diff = abs(len(self.lis) - len(self.lis2))
        if diff >= 2 or (self.lis2 and self.lis and self.lis2[0] < -self.lis[0]):
            small = heapq.heappop(self.lis)
            heapq.heappush(self.lis2, -small)
        diff = abs(len(self.lis) - len(self.lis2))
        if diff >= 2:
            small = heapq.heappop(self.lis2)
            heapq.heappush(self.lis, -small)       


    def findMedian(self) -> float:
        if len(self.lis) == len(self.lis2):
            s = self.lis[0]
            v = self.lis2[0]
            return (-s + v) / 2
        elif len(self.lis) > len(self.lis2):
            return -self.lis[0]
        else:
            return self.lis2[0]

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()