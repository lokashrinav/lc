
class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyCircularDeque:

    def __init__(self, k: int):
        self.cap = k
        self.size = 0   
        self.head = None
        self.tail = None     
    
    def printNode(self, node):
        while node:
            print(node.val, end="")
            node = node.next
        print("")
        
    def insertFront(self, value: int) -> bool:
        if self.isFull(): return False
        if not self.head:
            self.head = ListNode(value)
            self.tail = self.head
        else:
            newNode = ListNode(value)
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.size += 1
        return True
        
    def insertLast(self, value: int) -> bool:
        if self.isFull(): return False
        if not self.head:
            self.head = ListNode(value)
            self.tail = self.head
        else:
            newNode = ListNode(value)
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty(): return False
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head.next.prev = None
            self.head = self.head.next
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty(): return False
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            prev = self.tail.prev
            self.tail.prev.next = None
            self.tail = prev
        self.size -= 1
        return True

    def getFront(self) -> int:
        return self.head.val if self.head else -1      

    def getRear(self) -> int:
        return self.tail.val if self.tail else -1
        
    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.cap
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()