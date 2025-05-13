class Solution:
    def isArmstrong(self, n: int) -> bool:

        k = len(str(n))
        total = 0
        for elem in str(n):
            total += int(elem) ** k
        
        return total == n