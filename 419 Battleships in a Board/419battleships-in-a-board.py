class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:

        total = 0
        for y in range(len(board)):
            count = 0
            for x in range(len(board[0])):
                if board[y][x] == 'X':
                    if count == 0 and (y == 0 or board[y - 1][x] == '.'):
                        total += 1
                        count += 1
                else:
                    count = 0
        
        return total
            


        