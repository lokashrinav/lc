class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        
        for i in range(len(grid)):
            y, x = i, 0
            nums = []
            while y < len(grid) and x < len(grid):
                nums.append(grid[y][x])
                x += 1
                y += 1
            nums.sort(reverse=True)
            p = 0
            y, x = i, 0
            while y < len(grid) and x < len(grid):
                grid[y][x] = nums[p]
                p += 1
                x += 1
                y += 1

        # print(grid)
        
        for i in range(1, len(grid)):
            y, x = 0, i
            nums = []
            while y < len(grid) and x < len(grid):
                nums.append(grid[y][x])
                x += 1
                y += 1
            nums.sort()
            p = 0
            y, x = 0, i
            while y < len(grid) and x < len(grid):
                grid[y][x] = nums[p]
                p += 1
                x += 1
                y += 1

        # print(grid)

        return grid
            