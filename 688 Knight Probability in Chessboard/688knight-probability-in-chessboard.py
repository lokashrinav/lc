class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        moves = [(2, 1), (-2, 1), (1, 2), (1, -2), (2, -1), (-2, -1), (-1, 2), (-1, -2)]
        dp = {}

        def dfs(k, pos):
            #print(k, pos)
            if k == 0:
                return 1
            
            if (pos, k) in dp:
                return dp[(pos, k)]

            y, x = pos
            total = 0
            for dy, dx in moves:
                ny = dy + y
                nx = dx + x
                if ny >= 0 and ny < n and nx >= 0 and nx < n:
                    total += (dfs(k - 1, (ny, nx)) / 8)

            dp[(pos, k)] = total

            #print(pos, total)

            return total

        return dfs(k, (row, column))