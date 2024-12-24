class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class FrontMiddleBackQueue:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def pushFront(self, val: int) -> None:
        self.queue1.appendleft(val)
        if len(self.queue1) > len(self.queue2) + 1:
            out = self.queue1.pop()
            self.queue2.appendleft(out)
        print(self.queue1, self.queue2)

    def pushMiddle(self, val: int) -> None:
        if len(self.queue1) + 1 > len(self.queue2) + 1:
            out = self.queue1.pop()
            self.queue2.appendleft(out)
        self.queue1.append(val)
        #print(self.queue1, self.queue2)

    def pushBack(self, val: int) -> None:
        self.queue2.append(val)
        if len(self.queue1) < len(self.queue2):
            out = self.queue2.popleft()
            self.queue1.append(out)
        #print(self.queue1, self.queue2)

    def popFront(self) -> int:
        if not self.queue1:
            return -1
        put = self.queue1.popleft()
        if len(self.queue1) < len(self.queue2):
            out = self.queue2.popleft()
            self.queue1.append(out)
        #print(self.queue1, self.queue2)
        return put

    def popMiddle(self) -> int:
        if not self.queue1:
            return -1
        put = self.queue1.pop()
        if len(self.queue1) < len(self.queue2):
            out = self.queue2.popleft()
            self.queue1.append(out)
        #print(self.queue1, self.queue2)
        return put

    def popBack(self) -> int:
        if not self.queue1 and not self.queue2:
            return -1
        if not self.queue2:
            return self.queue1.pop()
        put = self.queue2.pop()
        if len(self.queue1) > len(self.queue2) + 1:
            out = self.queue1.pop()
            self.queue2.appendleft(out)
        return put

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()