class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        arr = [[""] * 3 for i in range(3)]

        for i in range(3):
            for p in range(3):
                if board[i][p] == 'X':
                    arr[i][p] = "X"
                elif board[i][p] == "O":
                    arr[i][p] == "O"
        
        def win(board, player):
            wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

            for x, y, z in wins:
                if board[x // 3][x % 3] == board[y // 3][y % 3] == board[z // 3][z % 3] == player:
                    return True
            
            return False

        one = 0
        zero = 0
        for elem in board:
            one += elem.count("X")
            zero += elem.count("O")
        
        if one != zero and zero + 1 != one:
            return False
        
        if win(board, "X") and win(board, "O"):
            return False
        
        if win(board, "X"):
            if zero + 1 != one:
                return False
        elif win(board, "O"):
            if zero != one:
                return False
        
        return True

        
        
        
