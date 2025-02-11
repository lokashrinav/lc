class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []

        first = list(part)

        for i in range(len(s)):
            stack.append(s[i])
            if len(stack) >= len(part):
                n = len(part)
                if stack[-n:] == first:
                    del stack[-n:]
        
        return ''.join(stack)