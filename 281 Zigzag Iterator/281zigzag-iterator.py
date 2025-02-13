class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.first = 0
        self.second = 0
        self.flag = True

    def next(self) -> int:
        if self.flag and self.first >= len(self.v1):
            self.flag = False
        elif not self.flag and self.second >= len(self.v2):
            self.flag = True

        if self.flag:
            self.flag = False
            self.first += 1
            return self.v1[self.first - 1]
        else:
            self.flag = True
            self.second += 1
            return self.v2[self.second - 1]

    def hasNext(self) -> bool:
        return self.first + self.second != len(self.v1) + len(self.v2)
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())