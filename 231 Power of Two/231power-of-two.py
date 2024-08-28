class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and log(n, 2) % 1 == 0



        