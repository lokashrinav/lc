class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [[0] * n for i in range(n)]
        hsetX = set()
        hsetY = set()
        hsetDiag1 = set()
        hsetDiag2 = set()
        count = [0]
        def dfs(hsetX, hsetY, hsetDiag1, hsetDiag2, curr, p):
            if curr == n:
                count[0] += 1
                return

            for i in range(len(board[0])):
                if board[p][i] == 0 and i not in hsetX and p not in hsetY and i - p not in hsetDiag1 and i + p not in hsetDiag2:
                    board[p][i] = 1
                    hsetX.add(i)
                    hsetY.add(p)
                    hsetDiag1.add(i - p)
                    hsetDiag2.add(i + p)
                    dfs(hsetX, hsetY, hsetDiag1, hsetDiag2, curr + 1, p + 1)
                    hsetX.remove(i)
                    hsetY.remove(p)
                    hsetDiag1.remove(i - p)
                    hsetDiag2.remove(i + p)
                    board[p][i] = 0  
            
            return

        dfs(hsetX, hsetY, hsetDiag1, hsetDiag2, 0, 0)
        return count[0]
        

        
        