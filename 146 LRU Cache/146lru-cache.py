class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hmap = {}
        self.head = None
        self.tail = None
    
    def printNodes(self, node):
        while node:
            print(node.key, node.val, end=" ")
            node = node.next
        print("ffun")        
            
    def get(self, key: int) -> int:
        #self.printNodes(self.head)

        if key in self.hmap:
            newNode = self.hmap[key]
            if self.head == self.tail:
                return self.hmap[key].val
            elif newNode == self.head:
                self.head = self.head.next
                self.head.prev = None
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = self.tail.next
                return self.hmap[key].val
            elif newNode == self.tail:
                return self.hmap[key].val
            else:
                newNode.prev.next = newNode.next
                newNode.next.prev = newNode.prev
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = self.tail.next
            return self.hmap[key].val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:

        if not self.head:
            newNode = Node(key, value)
            self.hmap[key] = newNode
            self.head = self.tail = newNode
        else:
            if key in self.hmap:
                self.hmap[key].val = value
                self.get(key)
            else:
                newNode = Node(key, value)
                self.hmap[key] = newNode
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = self.tail.next

            if len(self.hmap.keys()) > self.cap:
                self.head.next.prev = None
                del self.hmap[self.head.key]
                self.head = self.head.next
        
        #self.printNodes(self.head)
        
            


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)