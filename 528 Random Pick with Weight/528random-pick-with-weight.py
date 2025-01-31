class Solution:

    def __init__(self, w: List[int]):
        self.res = []
        total = 0
        for i in range(len(w)):
            total += w[i]
            self.res.append(total)

    def pickIndex(self) -> int:
        # [1, 3, 7, 10] --- 6
        x = random.uniform(0, self.res[-1])
        l, r = 0, len(self.res) - 1
        while l < r:
            m = (l + r) // 2
            if self.res[m] < x:
                l = m + 1
            else:
                r = m
        return l

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()