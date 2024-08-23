class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        visited = set()
        def checkValid(ind):
            y, x = ind
            if ind in visited or not (y >= 0 and y < len(board) and x >= 0 and x < len(board[0])):
                return False

        def dfs(ind, i):
            if checkValid(ind) == False:
                return False
            y, x = ind
            if board[y][x] == word[i] and i == len(word) - 1:
                return True
            visited.add(ind)
            if board[y][x] == word[i]:
                found = dfs((y + 1, x), i + 1) or dfs((y - 1, x), i + 1) or dfs((y, x + 1), i + 1) or dfs((y, x - 1), i + 1)
                visited.remove(ind)
                return found
            visited.remove(ind)
            return False
    
        for y in range(len(board)):
            for x in range(len(board[0])):
                if dfs((y, x), 0) == True:
                    return True
        
        return False

        

        