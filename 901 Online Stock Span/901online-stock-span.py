class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        stack = self.stack

        curr = 0 if not stack else stack[-1][1] + 1
    
        while stack and stack[-1][0] <= price:
            item, ind = stack.pop()

        saved = curr - stack[-1][1] if stack else curr + 1

        stack.append((price, curr))

        return saved



        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)