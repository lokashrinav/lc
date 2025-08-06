class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        curr = [0, 0]

        for i in range(len(commands)):
            if commands[i] == "RIGHT":
                curr[1] += 1
            elif commands[i] == "DOWN":
                curr[0] += 1
            elif commands[i] == "UP":
                curr[0] -= 1
            else:
                curr[1] -= 1
        
        return curr[0] * n + curr[1]
        