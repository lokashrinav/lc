class TwoSum:

    def __init__(self):
        self.arr = []

    def add(self, number: int) -> None:
        self.arr.append(number)

    def find(self, value: int) -> bool:
        hset = set()
        for i in range(len(self.arr)):
            if (value - self.arr[i]) in hset:
                return True
            else:
                hset.add(self.arr[i])
        return False
            

        
                


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)