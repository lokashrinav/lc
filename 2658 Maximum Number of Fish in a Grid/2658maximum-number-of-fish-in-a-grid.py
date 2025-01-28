class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(y, x):
            if not (y >= 0 and x >= 0 and x < len(grid[0]) and y < len(grid)) or (y, x) in visited or grid[y][x] == 0:
                return 0
            total = grid[y][x]
            visited.add((y, x))
            for i in range(len(directions)):
                ny, nx = y + directions[i][0], x + directions[i][1]
                total += dfs(ny, nx)
            return total
            
        y, x = len(grid), len(grid[0])
        visited = set()
        directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        maxNum = 0
        for i in range(y):
            for p in range(x):
                maxNum = max(dfs(i, p), maxNum)
        return maxNum

        