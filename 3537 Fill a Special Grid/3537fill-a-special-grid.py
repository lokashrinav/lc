class Solution:
    def specialGrid(self, N: int) -> List[List[int]]:

        def dfs(fun, total):
            matrix = [[total] * (2 ** fun) for i in range(2 ** fun)]
            
            if fun == 0:
                return matrix

            half = 2 ** (fun - 1)
            full = 2 ** fun
        
            arr = [[0, 0], [half, 0], [half, half], [0, half]]

            for p in range(4):
                y, x = arr[p]
                returned = dfs(fun - 1, total)
                total -= half * half
                            
                for i in range(y, y + half):
                    for v in range(x, x + half):
                        matrix[i][v] = returned[i - y][v - x]

            return matrix
                        
        
        matrix = [[0] * (2 ** N) for i in range(2 ** N)]

        if N == 0:
            return matrix

        half = 2 ** (N - 1)
        full = 2 ** N

        total = full * full - 1

        arr = [[0, 0], [half, 0], [half, half], [0, half]]

        for p in range(4):
            y, x = arr[p]
            returned = dfs(N - 1, total)
            total -= half * half
            
            for i in range(y, y + half):
                for v in range(x, x + half):
                    matrix[i][v] = returned[i - y][v - x]
        
        return matrix
           
    