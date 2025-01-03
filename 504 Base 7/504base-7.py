class Solution:
    def convertToBase7(self, num: int) -> str:
        
        if num == 0:
            return "0"

        res = ""
        neg = "-" if num < 0 else ""
        num = abs(num)

        while num != 0:
            rem = num % 7
            num = num // 7
            res = str(rem) + res
        
        return neg + res
        