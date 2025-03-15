class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            hset = set()
            for p in range(9):
                if board[i][p] in hset:
                    return False
                if board[i][p] != '.':
                    hset.add(board[i][p])

        for i in range(9):
            hset = set()
            for p in range(9):
                if board[p][i] in hset:
                    return False
                if board[p][i] != '.':
                    hset.add(board[p][i])

        for i in range(0, 9, 3):
            for p in range(0, 9, 3):
                hset = set()
                for a in range(i, i + 3):
                    for b in range(p, p + 3):
                        if board[a][b] in hset:
                            return False
                        if board[a][b] != '.':
                            hset.add(board[a][b])
        return True
            
            

