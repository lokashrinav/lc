class Solution:
    def judgeCircle(self, moves: str) -> bool:
        y, x = 0, 0

        for i in range(len(moves)):
            if moves[i] == "U":
                y += 1
            elif moves[i] == "D":
                y -= 1
            elif moves[i] == "L":
                x += 1
            elif moves[i] == "R":
                x -= 1
        
        return 0 == y and x == 0
        