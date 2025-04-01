class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        
        maxNum = 0

        def valid(index):
            y, x = index
            if y >= 1 and x >= 1 and x < len(grid[0]) - 1 and y < len(grid) - 1:
                return grid[y + 1][x + 1] + grid[y - 1][x - 1] + grid[y - 1][x + 1] + grid[y + 1][x - 1] + grid[y + 1][x] + grid[y - 1][x] + grid[y][x]
            
            return None


        for y in range(len(grid)):
            for x in range(len(grid[0])):
                calc = valid((y, x))
                if calc is not None:
                    maxNum = max(maxNum, calc)

        return maxNum