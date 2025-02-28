class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if not s and len(t) == 1 or len(s) == 1 and not t:
            return True

        if len(s) > len(t):
            final = 0
            for i in range(len(t)):
                if s[i] != t[i]:
                    return s[i+1:] == t[i:]
                final = i
            return abs(len(s) - 1 - final) <= 1
        elif len(s) < len(t):
            final = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    return t[i+1:] == s[i:]
                final = i
            return abs(len(t) - 1 - final) == 1
        else:
            for i in range(len(s)):
                if s[i] != t[i]:
                    return t[i+1:] == s[i+1:]
        
        return False
