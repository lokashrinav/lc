class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        '''
        ()
        ()()
        (())
        '''
        stack = []
        curr = 0
        for i in range(len(s)):
            elem = s[i]
            if elem == "(":
                stack.append(curr)
                curr = 0
            else:
                now = stack.pop()
                if s[i - 1] == "(":
                    curr += 1
                else: 
                    curr *= 2
                curr += now

            print(curr, stack)
        
        return curr
            

