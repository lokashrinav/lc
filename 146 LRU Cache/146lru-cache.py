class Node:
    def __init__(self, key, val):
        self.next = None
        self.prev = None
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hmap = {}
        self.head = None
        self.tail = None
        self.curr_cap = 0
    
    def printNode(self, node):
        print(None if not self.head else self.head.key, None if not self.tail else self.tail.key)

        while node:
            print(node.key, node.val)
            node = node.next
        print(" ")

    def printNode2(self, node):
        print(None if not self.head else self.head.key, None if not self.tail else self.tail.key)

        while node:
            print(node.key, node.val)
            node = node.prev
        print(" ")

    def get(self, key: int) -> int:
        if key not in self.hmap:
            return -1
        
        if key == self.head.key:
            return self.head.val

        #self.printNode2(self.tail)
            
        curr = self.hmap[key]
        out = curr.val

        if curr.prev:
            curr.prev.next = curr.next

        if curr.next:
            curr.next.prev = curr.prev

        if self.tail != self.head:
            if self.head != curr:
                curr.next = self.head
                self.head.prev = curr
            if curr == self.tail:
                self.tail = curr.prev
                

        curr.prev = None
        self.head = curr

        return out

    def put(self, key: int, value: int) -> None:
        #self.printNode2(self.tail)

        if key not in self.hmap:
            if self.curr_cap == self.cap:
                if self.head == self.tail:
                    self.head = None

                if self.tail.prev:
                    self.tail.prev.next = None
                del self.hmap[self.tail.key]
                self.tail = self.tail.prev
                self.curr_cap -= 1

            curr = self.hmap[key] = Node(key, value)
            curr.next = self.head

            if self.head:
                self.head.prev = curr
                
            if not self.head:
                self.tail = curr

            self.head = curr
            self.curr_cap += 1
        else:
            self.hmap[key].val = value
            self.get(key)
        



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)