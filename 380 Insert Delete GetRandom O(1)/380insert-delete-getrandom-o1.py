class RandomizedSet:

    def __init__(self):
        self.hmap = {}
        self.arr = []        

    def insert(self, val: int) -> bool:
        if val not in self.hmap:
            self.arr.append(val)
            self.hmap[val] = len(self.arr) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.hmap:
            return False
        ind = self.hmap[val]
        self.hmap[self.arr[-1]] = ind
        self.arr[ind], self.arr[-1] = self.arr[-1], self.arr[ind]
        self.arr.pop()
        del self.hmap[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()