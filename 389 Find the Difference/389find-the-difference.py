class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        p1, p2 = 0, 0
        while p2 < len(t):
            if p1 == len(s):
                return t[-1]
            if t[p2] != s[p1]:
                return t[p2]
            p1 += 1
            p2 += 1
        
            
        