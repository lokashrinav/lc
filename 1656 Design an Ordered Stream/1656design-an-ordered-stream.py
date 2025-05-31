class OrderedStream:

    def __init__(self, n: int):
        self.idk = [None] * n
        self.ind = 0
        
    def insert(self, idKey: int, value: str) -> List[str]:
        idk = self.idk

        idk[idKey - 1] = value
        res = []
        for i in range(self.ind, len(self.idk)):
            if idk[i] is not None:
                res.append(idk[i])
            else:
                self.ind = i
                break
        


        return res

        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)