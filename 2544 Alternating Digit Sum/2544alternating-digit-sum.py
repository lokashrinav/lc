class Solution:
    def alternateDigitSum(self, n: int) -> int:

        s = str(n)
        total = 0
        mult = 1

        for elem in s:
            total += int(elem) * mult
            mult = -mult

        return total

        