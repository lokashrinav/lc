class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hmap = {')':'(', '}':'{', ']':'['}
        for i in range(len(s)):
            if s[i] in '({[':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                elif hmap[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return not stack

        