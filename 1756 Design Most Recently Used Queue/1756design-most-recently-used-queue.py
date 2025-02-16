class MRUQueue:

    def __init__(self, n: int):
        self.idk = [i for i in range(1, n + 1)]        
        
    def fetch(self, k: int) -> int:
        n = self.idk.pop(k - 1)
        self.idk.append(n)
        return n
        


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)