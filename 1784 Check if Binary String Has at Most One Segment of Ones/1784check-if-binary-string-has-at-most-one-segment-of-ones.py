class Solution:
    def checkOnesSegment(self, s: str) -> bool:

        pos = True if s[0] == "1" else False
        for i in range(1, len(s)):
            if s[i] == "1" and pos and s[i - 1] == "0":
                return False

            if s[i] == "1":
                pos = 1
        
        return True

        