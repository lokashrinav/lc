class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.priority_queue = nums
        self.k = k
        heapq.heapify(self.priority_queue)
        while len(self.priority_queue) > k:
            heapq.heappop(self.priority_queue)

    def add(self, val: int) -> int:
        heapq.heappush(self.priority_queue, val)
        if len(self.priority_queue) > self.k:
            heapq.heappop(self.priority_queue)

        return self.priority_queue[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)