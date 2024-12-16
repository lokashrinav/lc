class RandomizedSet:

    def __init__(self):
        self.hmap = {}
        self.lis = []
        
    def insert(self, val: int) -> bool:
        if val in self.hmap.keys():
            return False
        self.lis.append(val)
        self.hmap[val] = len(self.lis) - 1
        return True



    def remove(self, val: int) -> bool:
        if val not in self.hmap.keys():
            return False
        saved = self.lis[-1]
        saved2 = self.hmap[val]
        self.lis[self.hmap[val]], self.lis[-1] = self.lis[-1], self.lis[self.hmap[val]] 
        self.lis.pop()
        self.hmap[saved] = saved2
        del self.hmap[val]
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.lis)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()