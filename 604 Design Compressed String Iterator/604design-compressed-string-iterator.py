class StringIterator:

    def __init__(self, compressedString: str):
        
        self.hmap = defaultdict(int)

        res = []

        num = [[]]

        for i in range(len(compressedString)):
            if compressedString[i].isalpha():
                res.append(compressedString[i])
                if num[-1]:
                    num.append([])
            else:
                num[-1].append(compressedString[i])
            
        print(num)

        for i in range(len(num)):
            num[i] = ''.join(num[i])
        
        for i in range(len(res)):
            self.hmap[i] = int(num[i])
        
        for i in range(len(res)):
            res[i] = (i, res[i])
        
        self.queue = deque(res)

        print(self.queue, self.hmap)

    def next(self) -> str:
        if self.queue:
            self.hmap[self.queue[0][0]] -= 1
            if self.hmap[self.queue[0][0]] == 0:
                saved = self.queue.popleft()
                return saved[1]
            else:
                return self.queue[0][1]
        else:
            return " "

    def hasNext(self) -> bool:
        return True if self.queue else False
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()