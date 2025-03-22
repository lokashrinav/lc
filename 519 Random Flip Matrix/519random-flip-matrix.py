class Solution:

    def __init__(self, m: int, n: int):
        # o(m * n)
        # o(m * n)
        self.m = m
        self.n = n
        self.hmap = {}
        self.total = m * n
        self.rem = self.total

    def flip(self) -> List[int]:
        x = randint(0, self.rem - 1)

        self.rem -= 1

        y = self.hmap.get(x, x)

        self.hmap[x] = self.hmap.get(self.rem, self.rem)

        return [y // self.n, y % self.n]



    def reset(self) -> None:
        self.hmap.clear()
        self.rem = self.total
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()