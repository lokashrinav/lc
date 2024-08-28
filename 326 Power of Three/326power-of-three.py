class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        while True:
            if n == 1:
                return True
            if n <= 0 or n % 1:
                return False
            n = n / 3
        return False

        