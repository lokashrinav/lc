class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        prod, sum1 = 1, 0
        for elem in str(n):
            sum1 += int(elem)
            prod *= int(elem)

        return prod - sum1
        