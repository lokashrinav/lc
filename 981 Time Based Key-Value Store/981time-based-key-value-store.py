class TimeMap:

    def __init__(self):
        self.hmap = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hmap:
            self.hmap[key] = []
        self.hmap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hmap:
            return ""
        l, r = 0, len(self.hmap[key]) - 1
        while l <= r:
            m = (l + r) // 2
            if self.hmap[key][m][0] == timestamp:
                return self.hmap[key][m][1]
            elif self.hmap[key][m][0] > timestamp:
                r = m - 1
            else:
                l = m + 1
        if self.hmap[key][m][0] > timestamp and m == 0:
            return ""
        elif self.hmap[key][m][0] > timestamp:
            return self.hmap[key][m - 1][1]
        return self.hmap[key][m][1]
        

        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)