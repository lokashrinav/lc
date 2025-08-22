class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for elem in s:
            if elem == '*':
                stack.pop()
            else:
                stack.append(elem)
        
        return ''.join(stack)