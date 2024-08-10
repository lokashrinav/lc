class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        
        i = 0
        minus_bool = 0
        plus_bool = 0
        zero_bool = 0
        while i < len(s) and (s[i] == " " or s[i] == "+" or s[i] =='-' or s[i] == "0"):
            if s[i] == "+":
                if zero_bool == 1 or minus_bool == 1 or plus_bool == 1:
                    return 0
                plus_bool = 1
            if s[i] == "-":
                if zero_bool == 1 or plus_bool == 1 or minus_bool == 1:
                    return 0   
                minus_bool = 1
            if s[i] == "0":
                zero_bool = 1
            if s[i] == " " and (zero_bool == 1 or plus_bool or minus_bool):
                return 0
            i += 1
        
        if i == len(s):
            return 0
        
        digits = ""
        numbers = set()
        for p in range(10):
            numbers.add(str(p))
        
        while i < len(s):
            if s[i] not in numbers:
                break
            digits += s[i]
            i += 1
        
        if not digits:
            return 0
        
        if minus_bool == 1 and -int(digits) < -(2 ** 31): 
            return -(2 ** 31)
        elif minus_bool == 0 and int(digits) > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif minus_bool == 1:
            return -int(digits)
        else:
            return int(digits)
            
        