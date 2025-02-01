class MovingAverage:

    def __init__(self, size: int):
        self.cap = size
        self.total = 0
        self.queue = deque()
        
    def next(self, val: int) -> float:
        if len(self.queue) == self.cap:
            x = self.queue.popleft()
            self.total -= x
        self.queue.append(val)
        self.total += val
        return self.total / len(self.queue)
            
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)