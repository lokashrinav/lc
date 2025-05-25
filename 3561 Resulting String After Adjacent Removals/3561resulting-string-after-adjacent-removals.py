class Solution:
    def resultingString(self, s: str) -> str:

        stack = []

        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
            else:
                if abs(ord(s[i]) - ord(stack[-1])) == 1 or abs(ord(s[i]) - ord(stack[-1])) == 25:
                    stack.pop()
                else:
                    stack.append(s[i])

        return ''.join(stack)
            
        