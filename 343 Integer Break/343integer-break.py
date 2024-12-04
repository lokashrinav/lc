class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1 

        count_of_3 = n // 3
        remainder = n % 3

        if remainder == 1:
            count_of_3 -= 1
            remainder += 3 

        return (3 ** count_of_3) * max(1, remainder)




