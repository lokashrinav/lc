class DetectSquares:

    def __init__(self):
        self.hmap = {}
        

    def add(self, point: List[int]) -> None:
        if tuple(point) in self.hmap:
            self.hmap[tuple(point)] += 1
        else:
            self.hmap[tuple(point)] = 1
        

    def count(self, point: List[int]) -> int:
        count = 0
        x2, y2 = point
        for x1, y1 in self.hmap.keys():
            if (abs(y1 - y2) != abs(x1 - x2)) or x1 == x2 or y1 == y2:
                continue
            if (x1, y2) in self.hmap and (x2, y1) in self.hmap:
                count += (self.hmap[(x1, y2)] * self.hmap[(x2, y1)] * self.hmap[(x1, y1)])
        return count


            
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)