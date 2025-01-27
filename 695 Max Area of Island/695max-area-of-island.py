class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]

        def dfs(node):
            y, x = node
            if y < 0 or x < 0 or x >= len(grid[0]) or y >= len(grid) or (y, x) in visited or grid[y][x] == 0:
                return 0

            visited.add((y, x))
            total = 1
            for i in range(len(directions)):
                ny, nx = directions[i][0] + y, directions[i][1] + x
                total += dfs((ny, nx))

            return total

        maxNum = 0
        for i in range(len(grid)):
            for p in range(len(grid[0])):
                if grid[i][p] == 1:
                    maxNum = max(maxNum, dfs((i, p)))
        
        return maxNum




        