class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:

        def func(y, x):
            res = []
            for i in range(y, y + k):
                for p in range(x, x + k):
                    res.append(grid[i][p])

            res.sort()

            minDist = float('inf')
            
            for i in range(1, len(res)):
                if res[i] != res[i - 1]:
                    minDist = min(abs(res[i] - res[i - 1]), minDist)

            return minDist if minDist != float('inf') else 0

        final = [[0] * (len(grid[0]) - k + 1) for i in range(len(grid)- k + 1)]

        for y in range(len(grid) - k + 1):
            for x in range(len(grid[0]) - k + 1):
                final[y][x] = func(y, x)

        return final
                
                
                
        