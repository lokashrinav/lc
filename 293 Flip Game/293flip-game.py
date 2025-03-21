class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        
        res = []
        for ind in range(len(currentState) - 1):
            if currentState[ind:ind+2] == "++":
                res.append(currentState[:ind] + '--' + currentState[ind+2:])
        
        return res

