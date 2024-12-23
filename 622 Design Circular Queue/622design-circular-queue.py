class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None  

class MyCircularQueue:

    def __init__(self, k: int):
        self.cap = k
        self.size = 0
        self.head = None
        self.tail = None       

    def enQueue(self, value: int) -> bool:
        if self.size + 1 > self.cap:
            return False

        if not self.head and not self.tail:
            self.head = ListNode(value)
            self.tail = self.head
        else:
            self.tail.next = ListNode(value)
            self.tail = self.tail.next
        self.size += 1
        return True
        

    def deQueue(self) -> bool:
        if self.head:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            self.size -= 1
            return True
        return False        

    def Front(self) -> int:
        if not self.head:
            return -1
        return self.head.val

    def Rear(self) -> int:
        if not self.tail:
            return -1
        return self.tail.val
        
    def isEmpty(self) -> bool:
        if self.head == None:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.size == self.cap:
            return True
        else:
            return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()