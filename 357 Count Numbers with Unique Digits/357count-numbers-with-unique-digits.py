class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        elif n == 1:
            return 10

        num = 1
        calc = 9
        total = 0
        for i in range(1, n+1):
            if i == 1:
                calc = 9
            elif i == 2:
                calc = 9
            else:
                calc -= 1
            num = num * calc
            total += num

        return total + 1




        