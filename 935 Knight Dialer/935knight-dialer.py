class Solution:
    def knightDialer(self, n: int) -> int:
        
        memo = {}
        dirs = [[2, 1], [1, 2], [-2, 1], [-1, 2], [1, -2], [2, -1], [-1, -2], [-2, -1]]

        def dfs(curr, n):
            # print(curr, n)
            if n == 0:
                return 1
            
            if (curr, n) in memo:
                return memo[(curr, n)]

            y, x = curr
            
            total = 0
            for ny, nx in dirs:
                dy, dx = y + ny, x + nx
                if (dy, dx) == (3, 0) or (dy, dx) == (3, 2):
                    continue

                if 4 > dy >= 0 and 3 > dx >= 0: 
                    total += dfs((dy, dx), n - 1)

            memo[(curr, n)] = total % ((10 ** 9) + 7)

            return memo[(curr, n)]
        
        total = 0
        for i in range(4):
            for p in range(3):
                if (i, p) == (3, 0) or (i, p) == (3, 2):
                    continue
                calc = dfs((i, p), n - 1)
                # print((i, p), calc)
                total += calc
        
        return total % ((10 ** 9) + 7) 

        