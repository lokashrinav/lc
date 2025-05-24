class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:


        '''

        

        '''

        r = 0
        stack = []
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while stack and stack[-1] == popped[r]:
                stack.pop()
                r += 1
        
        return False if stack else True
        