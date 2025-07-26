class FrontMiddleBackQueue:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def pushFront(self, val: int) -> None:
        self.queue1.appendleft(val)
        if len(self.queue1) - len(self.queue2) >= 2:
            self.queue2.appendleft(self.queue1.pop())
        print(self.queue1, self.queue2)

    def pushMiddle(self, val: int) -> None:
        if len(self.queue1) > len(self.queue2):
            self.queue2.appendleft(self.queue1.pop())   
            self.queue1.append(val)
        else:
            self.queue1.append(val)

    def pushBack(self, val: int) -> None:
        self.queue2.append(val)
        if len(self.queue2) - len(self.queue1) >= 1:
            self.queue1.append(self.queue2.popleft())
        print(self.queue1, self.queue2)

    def popFront(self) -> int:
        if not self.queue1:
            return -1
        out = self.queue1.popleft()  
        if len(self.queue2) - len(self.queue1) >= 1:
            self.queue1.append(self.queue2.popleft())
        print(self.queue1, self.queue2)
        return out

    def popMiddle(self) -> int:
        if not self.queue1:
            return -1
        out = self.queue1.pop()
        if len(self.queue2) - len(self.queue1) >= 1:
            self.queue1.append(self.queue2.popleft())
        print(self.queue1, self.queue2)
        return out

    def popBack(self) -> int:
        if not self.queue1:
            return -1
        out = self.queue2.pop() if self.queue2 else self.queue1.pop()
        if len(self.queue1) - len(self.queue2) >= 2:
            self.queue2.appendleft(self.queue1.pop())   
        print(self.queue1, self.queue2)
        return out


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()