class FirstUnique:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.queue = deque()
        self.seen = set()
        self.hmap = defaultdict(int)

        for i in range(len(nums)):
            self.hmap[nums[i]] += 1
            if self.hmap[nums[i]] > 2:
                continue
            self.queue.append(nums[i])
        
        while self.queue and self.hmap[self.queue[0]] > 1:
            self.queue.popleft()
                    
    def showFirstUnique(self) -> int:
        return self.queue[0] if self.queue else -1
        
    def add(self, value: int) -> None:
        self.hmap[value] += 1
        if self.hmap[value] == 1:
            self.queue.append(value)
        else:
            while self.queue and self.hmap[self.queue[0]] > 1:
                self.queue.popleft()
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)