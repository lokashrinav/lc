class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        p1 = 0
        for i in range(len(t)):
            if p1 == len(s):
                return True
            if s[p1] == t[i]:
                p1 += 1
        
        return p1 == len(s)
            
        