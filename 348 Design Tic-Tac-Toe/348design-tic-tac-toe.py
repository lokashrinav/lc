class TicTacToe:

    def __init__(self, n: int):
        self.row = [0] * n
        self.col = [0] * n
        self.diag1 = 0
        self.diag2 = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        n = self.n
        idk = 1 if player == 1 else -1
        self.row[row] += idk
        self.col[col] += idk
        if row == col:
            self.diag1 += idk
        if row + col == n - 1:
            self.diag2 += idk
        
        if self.row[row] == n or self.col[col] == n or self.diag1 == n or self.diag2 == n:
            return 1
        elif self.row[row] == -n or self.col[col] == -n or self.diag1 ==- n or self.diag2 == -n:
            return 2
        else:
            return 0
        


        '''
        [1, 1, 1]
        [1, 1, 1]
        [1, 1, 1]

        [1, 1, 1, 1]
        [1, 1, 1, 1]
        [1, 1, 1, 1]
        [1, 1, 1, 1]
        '''
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)