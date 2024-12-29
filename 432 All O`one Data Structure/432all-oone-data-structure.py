class ListNode:
    def __init__(self, num=1):
        self.freq = num
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:
    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None
        self.small = None
        self.hmap = {}

    def printNode(self, node):
        while node:
            print(self.count, node.freq, node.keys)
            node = node.next
        self.count += 1
        print("")

    def inc(self, key: str) -> None:
        if key not in self.hmap:
            # exactly as you had it
            if not self.head:
                newNode = ListNode()
                newNode.keys.add(key)
                self.head = newNode
                self.tail = self.head
            else:
                self.head.keys.add(key)
            self.small = self.head
            self.hmap[key] = self.head
        else:
            # same structure, only fix the “middle” logic
            if self.hmap[key] == self.tail:
                newNode = ListNode(self.hmap[key].freq + 1)
                self.tail.keys.remove(key)
                if self.small == self.tail and len(self.tail.keys) == 0:
                    self.small = newNode
                newNode.keys.add(key)
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = newNode
                self.hmap[key] = self.tail
            else:
                node = self.hmap[key]
                oldFreq = node.freq
                node.keys.remove(key)
                if len(node.keys) == 0:
                    self.small = node.next
                # FIX: check if node.next already has freq = oldFreq + 1
                if node.next and node.next.freq == oldFreq + 1:
                    node.next.keys.add(key)
                    self.hmap[key] = node.next
                else:
                    # create a new node in-between
                    newNode = ListNode(oldFreq + 1)
                    newNode.keys.add(key)
                    newNode.prev = node
                    newNode.next = node.next
                    if node.next:
                        node.next.prev = newNode
                    node.next = newNode
                    if node == self.tail:
                        self.tail = newNode
                    self.hmap[key] = newNode

    def dec(self, key: str) -> None:
        node = self.hmap[key]
        # same overall structure, add freq checks
        if node == self.tail and node == self.head:
            if len(node.keys) == 1:
                self.head = None
                self.tail = None
                self.small = None
            else:
                self.head.keys.remove(key)
                self.small = self.head
            del self.hmap[key]
        elif node == self.tail:
            # tail logic
            if len(node.keys) == 1 and node.freq == 1:
                node.keys.remove(key)
                del self.hmap[key]
                self.tail = node.prev
                if self.tail:
                    self.tail.next = None
                if node == self.small:
                    self.small = self.tail
            else:
                node.keys.remove(key)
                newFreq = node.freq - 1
                # If it goes down to 0, remove key altogether
                if newFreq == 0:
                    del self.hmap[key]
                else:
                    # check if node.prev has freq = newFreq
                    if node.prev and node.prev.freq == newFreq:
                        node.prev.keys.add(key)
                        self.hmap[key] = node.prev
                    else:
                        newNode = ListNode(newFreq)
                        newNode.keys.add(key)
                        newNode.next = node
                        newNode.prev = node.prev
                        if node.prev:
                            node.prev.next = newNode
                        else:
                            self.head = newNode
                        node.prev = newNode
                        self.hmap[key] = newNode
                if len(node.keys) == 0:
                    self.tail = node.prev
                    if self.tail:
                        self.tail.next = None
                    if node == self.small:
                        self.small = self.tail
        elif node == self.head:
            # head logic same as you had it
            node.keys.remove(key)
            del self.hmap[key]
            if len(node.keys) == 0 and node == self.small:
                while node and len(node.keys) == 0:
                    node = node.next
                self.small = node
        else:
            # middle node
            if node == self.small and len(node.keys) == 1:
                self.small = node.prev
            node.keys.remove(key)
            oldFreq = node.freq
            newFreq = oldFreq - 1
            if newFreq == 0:
                del self.hmap[key]
            else:
                # FIX: check if node.prev has freq = newFreq
                if node.prev and node.prev.freq == newFreq:
                    node.prev.keys.add(key)
                    self.hmap[key] = node.prev
                else:
                    newNode = ListNode(newFreq)
                    newNode.keys.add(key)
                    newNode.next = node
                    newNode.prev = node.prev
                    if node.prev:
                        node.prev.next = newNode
                    else:
                        self.head = newNode
                    node.prev = newNode
                    self.hmap[key] = newNode
            if len(node.keys) == 0:
                prevN, nextN = node.prev, node.next
                if prevN:
                    prevN.next = nextN
                else:
                    self.head = nextN
                if nextN:
                    nextN.prev = prevN
                else:
                    self.tail = prevN
                if node == self.small:
                    self.small = nextN

    def getMaxKey(self) -> str:
        if self.tail is None:
            return ""
        return next(iter(self.tail.keys))

    def getMinKey(self) -> str:
        if self.head is None:
            return ""
        return next(iter(self.small.keys))
