class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        
        matrix = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
        matrix2 = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]

        for y in range(len(grid)):
            count = 0
            for x in range(len(grid[0])):
                if grid[y][x] == 'E':
                    count += 1
                    matrix[y][x] = count
                elif grid[y][x] == '0':
                    matrix[y][x] = count
                else:
                    count = 0

        for y in range(len(grid)):
            maxSoFar = None
            for x in range(len(grid[0]) - 1, -1, -1):
                if maxSoFar is None:
                    maxSoFar = matrix[y][x]
                if grid[y][x] == '0':
                    matrix[y][x] = maxSoFar
                elif grid[y][x] == 'W':
                    maxSoFar = None
                else:
                    matrix2[y][x] = maxSoFar

        for x in range(len(grid[0])):
            count = 0
            for y in range(len(grid)):
                if grid[y][x] == 'E':
                    count += 1
                    matrix2[y][x] = count
                elif grid[y][x] == '0':
                    matrix2[y][x] = count
                else:
                    count = 0
        
        for x in range(len(grid[0])):
            maxSoFar = None
            for y in range(len(grid) - 1, -1, -1):
                if maxSoFar is None:
                    maxSoFar = matrix2[y][x]
                if grid[y][x] == '0':
                    matrix2[y][x] = maxSoFar
                elif grid[y][x] == 'W':
                    maxSoFar = None
                else:
                    matrix2[y][x] = maxSoFar
        
        maxNum = 0
        maxSoFar = None
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == '0':
                    if matrix[y][x] + matrix2[y][x] > maxNum:
                        maxNum = matrix[y][x] + matrix2[y][x]
                        maxSoFar = (y, x)
        
        return maxNum

        

        
                
                
        


        