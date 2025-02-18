class Logger:

    def __init__(self):
        self.hmap = defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.hmap:
            self.hmap[message] = timestamp + 10
            return True
        elif timestamp >= self.hmap[message]:
            self.hmap[message] = timestamp + 10
            return True

        return False
        

        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)