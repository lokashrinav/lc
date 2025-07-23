class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        '''

        aaxybb

        '''

        stack = []
        total = 0
        for i in range(len(s)):
            stack.append(s[i])
            if x > y:
                if stack[-2:] == ["a", "b"]:
                    total += x
                    stack.pop()
                    stack.pop()
            else:
                if stack[-2:] == ["b", "a"]:
                    total += y
                    stack.pop()
                    stack.pop()
        
        stack2 = []
        for i in range(len(stack)):
            stack2.append(stack[i])
            if x <= y:
                if stack2[-2:] == ["a", "b"]:
                    total += x
                    stack2.pop()
                    stack2.pop()
            else:
                if stack2[-2:] == ["b", "a"]:
                    total += y
                    stack2.pop()
                    stack2.pop()
        
        return total