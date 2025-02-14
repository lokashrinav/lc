class ProductOfNumbers:

    def __init__(self):
        self.stack = []

    def add(self, num: int) -> None:
        if num:
            if not self.stack:
                self.stack.append(num)
            else:
                self.stack.append(self.stack[-1] * num)
        else:
            self.stack = []           

    def getProduct(self, k: int) -> int:
        if len(self.stack) < k:
            return 0
        elif len(self.stack) == k:
            return self.stack[-1]
        else:
            return int(self.stack[-1] / self.stack[-k - 1])
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)