class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.hset = set(range(maxNumbers))

    def get(self) -> int:
        if len(self.hset):
            out = self.hset.pop()
            return out
        else:
            return -1
        
    def check(self, number: int) -> bool:
        return number in self.hset


    def release(self, number: int) -> None:
        self.hset.add(number)
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)