class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        
        total = 0
        for elem in str(x):
            total += int(elem)
        
        return total if x % total == 0 else -1
        