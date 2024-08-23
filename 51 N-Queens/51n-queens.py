class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [["."] * n for _ in range(n)]
        cols = set()
        posDiag = set()
        negDiag = set()
        res = []

        def valid(node):
            y, x = node
            if x in cols or y - x in negDiag or y + x in posDiag:
                return False
            return True

        def dfs(i):
            print(grid, i)
            for y in range(i, n):
                bool1 = False
                for x in range(n):
                    if grid[y][x] == "." and valid((y, x)):
                        if valid((y, x)):
                            grid[y][x] = "Q"
                            cols.add(x)
                            posDiag.add(y + x)
                            negDiag.add(y - x)
                            dfs(y + 1)
                            cols.remove(x)
                            posDiag.remove(y + x)
                            negDiag.remove(y - x)
                            grid[y][x] = "."
                if not bool1:
                    return False
            res.append([''.join(row) for row in grid])
                    
        dfs(0)

        return res
        