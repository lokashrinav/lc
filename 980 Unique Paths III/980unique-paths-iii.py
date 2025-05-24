class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        start = None
        count = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] != -1:
                    count += 1
                if grid[y][x] == 1:
                    start = (y, x)

        visited = set()
        visited.add(start)
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def dfs(y, x):
            if grid[y][x] == 2:
                #print(len(visited), count)
                if len(visited) == count:
                    return 1
                return 0
                        
            total = 0
            for ny, nx in dirs:
                dy, dx = y + ny, x + nx
                if (dy, dx) not in visited and len(grid) > dy >= 0 and len(grid[0]) > dx >= 0 and grid[dy][dx] != -1:
                    visited.add((dy, dx))
                    total += dfs(dy, dx)
                    visited.remove((dy, dx))
            
            return total

        y, x = start

        return dfs(y, x)
        