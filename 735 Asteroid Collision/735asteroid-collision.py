class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        '''

        5, 10, -5

        8, 5, 10, 2, -5, -8

        8, 5, 10

        '''

        stack = []

        for i in range(len(asteroids)):
            if asteroids[i] >= 0:
                stack.append(asteroids[i])
            else:
                out = None
                while stack and stack[-1] >= 0 and stack[-1] <= abs(asteroids[i]):
                    out = stack.pop()
                    if out == abs(asteroids[i]):
                        break
                
                if out == abs(asteroids[i]):
                    continue

                if not stack or stack[-1] < 0:
                    stack.append(asteroids[i])
        
        return stack