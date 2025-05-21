class Solution:
    def reverseDegree(self, s: str) -> int:
        
        sum1 = 0
        for i in range(len(s)):
            sum1 += (i+1) * (26 - (ord(s[i]) - 97))
        
        return sum1

        