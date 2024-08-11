class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def sudokuHelper():
            for y in range(9):
                for x in range(9):
                    if board[y][x] == ".":
                        for i in range(1, 10):
                            if isValid((y, x), i):
                                board[y][x] = str(i)
                                call = sudokuHelper()
                                if call:
                                    return True
                                board[y][x] = "."
                        return False
            return True

        def isValid(node, digit):
            y, x = node
            for i in range(9):
                if str(digit) == board[y][i]:
                    return False
                if str(digit) == board[i][x]:
                    return False
            
            rounded_x = 3 * (x // 3) 
            rounded_y = 3 * (y // 3) 

            for c in range(rounded_x, rounded_x + 3):
                for d in range(rounded_y, rounded_y + 3):
                    if board[d][c] == str(digit):
                        return False
            return True

        sudokuHelper()

        