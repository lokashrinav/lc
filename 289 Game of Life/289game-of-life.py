class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        ops = [[-1, 0], [0, -1], [1, 0], [0, 1], [-1, 1], [1, -1], [-1, -1], [1, 1]] 

        for i in range(len(board)):
            for p in range(len(board[0])):
                live = 0
                for y, x in ops:
                    ny, nx = y + i, p + x
                    if ny >= 0 and nx >= 0 and nx < len(board[0]) and ny < len(board):
                        if board[ny][nx] == 1 or board[ny][nx] == 3:
                            live += 1

                if board[i][p] == 1 and live < 2:
                    board[i][p] = 3
                elif board[i][p] == 1 and (live == 2 or live == 3):
                    board[i][p] = 1
                elif board[i][p] == 1 and live > 3:
                    board[i][p] = 3
                elif board[i][p] == 0 and live == 3:
                    board[i][p] = 2

        for i in range(len(board)):
            for p in range(len(board[0])):
                if board[i][p] == 2:
                    board[i][p] = 1
                elif board[i][p] == 3:
                    board[i][p] = 0
        
        return board