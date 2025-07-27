class Node:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.head = None
        self.tail = None
        self.cap = 0

    def enQueue(self, value: int) -> bool:
        if self.cap == self.k:
            return False

        self.cap += 1
        if not self.tail:
            self.tail = self.head = curr = Node(value)
            return True
        
        curr = Node(value)
        self.tail.next = curr
        curr.prev = self.tail
        self.tail = curr

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        if self.head.next:        
            self.head.next.prev = None
        
        if self.head == self.tail:
            self.tail = None
            
        self.head = self.head.next
        
        self.cap -= 1

        return True
        

    def Front(self) -> int:
        return self.head.val if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.tail.val if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.head is None

    def isFull(self) -> bool:
        return self.cap == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()