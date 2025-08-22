class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:

        maxY = 0
        minY = len(grid) - 1
        maxX = 0
        minX = len(grid[0]) - 1

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    maxY = max(maxY, y)
                    minY = min(minY, y)
                    maxX = max(maxX, x)
                    minX = min(minX, x)
        
        return (maxY - minY + 1) * (maxX - minX + 1)