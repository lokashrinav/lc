class LogSystem:

    def __init__(self):
        self.arr1 = []
        self.arr2 = []
        self.lis = ["Year", "Month", "Day", "Hour", "Minute", "Second"]

    def put(self, id: int, timestamp: str) -> None:
        ind = bisect_left(self.arr1, timestamp)
        self.arr1.insert(ind, timestamp)
        self.arr2.insert(ind, (timestamp, id))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        
        lis = self.lis
        idk = start.split(":")
        new = ""
        for i in range(min(lis.index(granularity) + 1, len(lis))):
            new += idk[i] + ":"
        
        for i in range(lis.index(granularity) + 1, len(lis)):
            new += "00:"
        new = new[:-1]

        idk = end.split(":")
        new2 = ""
        for i in range(min(lis.index(granularity) + 1, len(lis))):
            new2 += idk[i] + ":"
        
        for i in range(lis.index(granularity) + 1, len(lis)):
            new2 += "99:"
        new2 = new2[:-1]
        
        ind = bisect_left(self.arr1, new)
        ind2 = bisect_right(self.arr1, new2)

        res = []
        for i in range(ind, ind2):
            res.append(self.arr2[i][1])

        return res
                


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)