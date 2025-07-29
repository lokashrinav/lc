from copy import copy, deepcopy

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        diag = set()
        rev = set()

        board = [["."] * n for i in range(n)]

        final = []

        def dfs(ny):
            if ny == len(board):
                if len(cols) == len(board):
                    final.append(deepcopy(board))
                return len(cols) == len(board)

            for x in range(n):
                if x not in cols and (ny + x) not in diag and (ny - x) not in rev:
                    cols.add(x)
                    diag.add(ny + x)
                    rev.add(ny - x)
                    board[ny][x] = "Q"
                    dfs(ny + 1)
                    board[ny][x] = "."
                    cols.remove(x)
                    diag.remove(ny + x)
                    rev.remove(ny - x)

            return False
                    
        dfs(0)

        for i in range(len(final)):
            for p in range(len(final[i])):
                final[i][p] = ''.join(final[i][p])

        return final
                
