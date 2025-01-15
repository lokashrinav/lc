class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        while len(self.queue1) != 1:
            self.queue2.append(self.queue1.popleft())

        saved = self.queue1.popleft()

        while self.queue2:
            self.queue1.append(self.queue2.popleft())

        return saved
        
    def top(self) -> int:
        return self.queue1[-1]

    def empty(self) -> bool:
        if not self.queue1:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()