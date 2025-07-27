class Solution:
    def countSubstrings(self, s: str) -> int:
        
        total = len(s)
        for i in range(len(s)):
            p = 1
            while i - p >= 0 and i + p < len(s):
                if s[i - p] == s[i + p]:
                    total += 1
                else:
                    break
                p += 1
                
            p = 1
            while i - p >= 0 and i + p - 1 < len(s):
                if s[i - p] == s[i + p - 1]:
                    total += 1
                else:
                    break
                p += 1
        
        return total
            
                
         