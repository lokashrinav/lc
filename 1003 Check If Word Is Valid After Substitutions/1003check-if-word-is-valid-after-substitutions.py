class Solution:
    def isValid(self, s: str) -> bool:
        '''

        '''

        stack = []

        for i in range(len(s)):
            if s[i] == "a":
                stack.append(s[i])
            elif stack and s[i] == "b" and stack[-1] == "a":
                stack[-1] += "b"
            elif stack and s[i] == "c" and stack[-1] == "ab":
                stack.pop()
            else:
                return False
        
        return True if not stack else False
        