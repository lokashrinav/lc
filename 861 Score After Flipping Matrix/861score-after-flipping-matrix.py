class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        

        og = grid.copy()

        for i in range(len(grid)):
            if grid[i][0] == 0:
                for p in range(len(grid[0])):
                    grid[i][p] ^= 1

        for i in range(len(grid)):
            og[i][0] ^= 1

        for i in range(len(grid)):
            if og[i][0] == 0:
                for p in range(len(grid[0])):
                    og[i][p] ^= 1
                
        def weee(grid):
            for i in range(1, len(grid[0])):
                one = 0
                for p in range(len(grid)):
                    if grid[p][i] == 1:
                        one += 1
                
                if len(grid) - one > one:
                    for p in range(len(grid)):
                        grid[p][i] ^= 1
            
            total = 0
            for i in range(len(grid)):
                count = 0
                for p in range(len(grid[0])):
                    count += grid[i][p] * (2 ** (len(grid[0]) - p - 1))
                total += count
            
            return total

        return max(weee(grid), weee(og))




