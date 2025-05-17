class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        l, r = 0, 0
        total = 0

        for i in range(len(s)):
            if s[i] == "L":
                l += 1
            else:
                r += 1
            
            if r == l:
                total += 1
                l = r = 0
        
        return total


        