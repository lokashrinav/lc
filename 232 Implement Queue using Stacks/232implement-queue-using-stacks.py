class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def push(self, x: int) -> None:
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        self.stack1.append(x)
        
    def pop(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:     
        if self.stack1:
            return self.stack1[0]
        else:
            return self.stack2[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2

    # [1, 2] 

    # [4, 5, 6]   


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()