class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None   
        self.tail = None     
        self.size = 0

    def printNode(self, node):
        while node:
            print(node.val, end=" ")
            node = node.next
        print("")

    def get(self, index: int) -> int:
        if self.size <= index: return -1
        node = self.head
        while index:
            node = node.next
            index -= 1
        return node.val   

    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head = ListNode(val)
            self.tail = self.head
        else:
            newNode = ListNode(val)
            newNode.next = self.head
            self.head = newNode
        self.size += 1  
        #self.printNode(self.head)

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = ListNode(val)
            self.tail = self.head
        else:
            newNode = ListNode(val)
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1
        if self.size <= 3:
            self.printNode(self.head)

    def addAtIndex(self, index: int, val: int) -> None:
        if self.size < index: return -1
        if index == 0:
            self.addAtHead(val)
            return
        elif index == self.size:
            self.addAtTail(val)
            return
        node = self.head
        prev = None
        while index:
            prev = node
            node = node.next
            index -= 1

        prev.next = ListNode(val)
        prev.next.next = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if self.size <= index: return 1
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.size -= 1
            #self.printNode(self.head)
            return
        elif index == 0:
            self.head = self.head.next
            self.size -= 1
            #self.printNode(self.head)
            return

        node = self.head
        prev = None

        while index:
            prev = node
            node = node.next
            index -= 1

        if node:
            if node == self.tail:
                self.tail = prev
            prev.next = node.next
        else:
            prev.next = None

        self.size -= 1
        #self.printNode(self.head)

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)