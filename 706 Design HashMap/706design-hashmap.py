class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.arr = [None] * 1000

    def put(self, key: int, value: int) -> None:
        damn = hash(key) % 1000
        node = self.arr[damn]
        prev = None
        while node:
            if node.val[0] == key:
                node.val[1] = value
                return
            prev = node
            node = node.next
        if prev:
            prev.next = ListNode([key, value])
        else:
            self.arr[damn] = ListNode([key, value])

    def get(self, key: int) -> int:
        damn = hash(key) % 1000
        node = self.arr[damn]
        while node:
            if node.val[0] == key:
                return node.val[1]
            node = node.next
        return -1      

    def remove(self, key: int) -> None:
        damn = hash(key) % 1000
        node = self.arr[damn]
        prev = None

        while node:
            if node.val[0] == key:
                break
            prev = node
            node = node.next
        if not node:
            return

        if prev:
            prev.next = node.next
        else:
            self.arr[damn] = node.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)