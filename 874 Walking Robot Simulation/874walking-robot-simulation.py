class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:

        obstacles = set(tuple((y, x)) for x, y in obstacles)

        up = 0

        obstacles = set(obstacles)

        points = []
        maxDist = 0
        curr = (0, 0)

        def check(curr):
            nonlocal maxDist
            y, x = curr

            maxDist = max((y ** 2) + (x ** 2), maxDist)

            print(curr, points, maxDist)

        for i in range(len(commands)):
            if commands[i] == -2:
                up -= 1
                if up == -1:
                    up = 3
            elif commands[i] == -1:
                up += 1
                if up == 4:
                    up = 0
            else:
                if up == 0:
                    while (curr[0] + 1, curr[1]) not in obstacles and commands[i]:
                        curr = (curr[0] + 1, curr[1])
                        commands[i] -= 1
                elif up == 2:
                    while (curr[0] - 1, curr[1]) not in obstacles and commands[i]:
                        curr = (curr[0] - 1, curr[1])
                        commands[i] -= 1
                elif up == 3:
                    while (curr[0], curr[1] - 1) not in obstacles and commands[i]:
                        curr = (curr[0], curr[1] - 1)
                        commands[i] -= 1                
                else:
                    while (curr[0], curr[1] + 1) not in obstacles and commands[i]:
                        curr = (curr[0], curr[1] + 1)
                        commands[i] -= 1
            
                check(curr)
        
        return maxDist
            
        