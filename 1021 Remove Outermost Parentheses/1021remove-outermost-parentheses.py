class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        final = ""

        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                if len(stack) != 0:
                    final += s[i]
                stack.append("(")
            else:
                stack.pop()
                if len(stack) != 0:
                    final += s[i]
        
        return final

        