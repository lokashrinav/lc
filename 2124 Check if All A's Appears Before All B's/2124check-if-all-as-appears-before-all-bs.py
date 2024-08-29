class Solution:
    def checkString(self, s: str) -> bool:
        b = False
        for i in range(len(s)):
            if s[i] == 'a' and b:
                return False
            if s[i] == 'b':
                b = True
        return True

        