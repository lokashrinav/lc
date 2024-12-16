class RandomizedCollection:

    def __init__(self):
        self.hmap = {}
        self.lis = []
        
    def insert(self, val: int) -> bool:
        self.lis.append(val)
        if val in self.hmap.keys():
            self.hmap[val].append(len(self.lis) - 1)
            return False
        else:
            self.hmap[val] = [len(self.lis) - 1]
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hmap.keys():
            return False
        saved = self.lis[-1]
        saved2 = self.hmap[val][-1]
        self.lis[saved2], self.lis[-1] = self.lis[-1], self.lis[saved2] 
        self.hmap[saved].remove(len(self.lis) - 1)
        self.lis.pop()
        self.hmap[saved].append(saved2)
        self.hmap[val].pop()
        if self.hmap[val] == []:
            del self.hmap[val]
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.lis)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()