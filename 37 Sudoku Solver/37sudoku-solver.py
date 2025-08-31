class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]    
        boxes = [set() for _ in range(9)]  

        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    digit = board[r][c]
                    rows[r].add(digit)
                    cols[c].add(digit)
                    boxes[(r // 3) * 3 + c // 3].add(digit)
        
        def sudoku(board, start, end):

            #print(rows, cols)
            
            for y in range(start, len(board)):
                for x in range(0 if y > start else end, 9):
                    flag = True
                    if board[y][x] == ".":
                        for i in range(9):
                            box = (y // 3) * 3 + x // 3
                            if str(i + 1) in rows[y] or str(i + 1) in cols[x] or str(i + 1) in boxes[box]:
                                continue
                            flag = False
                            board[y][x] = str(i + 1)
                            rows[y].add(board[y][x])
                            cols[x].add(board[y][x])
                            boxes[box].add(board[y][x])

                            nexty, nextx = y + (1 if x == 8 else 0), x + (1 if x != 8 else -8) 
                            returned = sudoku(board, nexty, nextx)
                            if returned:
                                return True

                            rows[y].remove(board[y][x])
                            cols[x].remove(board[y][x])
                            boxes[box].remove(board[y][x])
                            board[y][x] = "."
    
                        return False
            
            return True
        
        return sudoku(board, 0, 0)

            