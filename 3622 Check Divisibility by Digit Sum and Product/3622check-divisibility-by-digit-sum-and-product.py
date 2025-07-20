class Solution:
    def checkDivisibility(self, n: int) -> bool:

        sum1 = sum(int(s) for s in str(n))
        prod1 = 1
        for elem in str(n):
            prod1 *= int(elem)

        return True if n % (sum1 + prod1) == 0 else False

        