class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0
        for i in range(len(s)):
            if s[i] == "(":
                leftMin += 1
                leftMax += 1
            if s[i] == ")":
                leftMin -= 1
                leftMax -= 1
            if s[i] == "*":
                leftMin -= 1
                leftMax += 1
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0
        