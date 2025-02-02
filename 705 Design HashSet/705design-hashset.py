class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for i in range(self.size)]

    def hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        h = self.hash(key)
        if key not in self.buckets[h]:
            self.buckets[h].append(key)
        
    def remove(self, key: int) -> None:
        ind = self.hash(key)
        if key in self.buckets[ind]:
            self.buckets[ind].remove(key)

    def contains(self, key: int) -> bool:
        ind = self.hash(key)
        if key in self.buckets[ind]:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)