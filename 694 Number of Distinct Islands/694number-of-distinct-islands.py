class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def dfs(pos, start):
            y, x = pos
            iy, ix = start
            curr.append(start)

            for ny, nx in dirs:
                dy, dx = ny + y, nx + x
                if ((dy, dx) not in visited) and dy >= 0 and dx >= 0 and dy < len(grid) and dx < len(grid[0]) and grid[dy][dx] == 1:
                    visited.add((dy, dx))
                    dfs((dy, dx), (iy + ny, ix + nx))
        
        comps = set()
        visited = set()

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if (y, x) not in visited and grid[y][x] == 1:
                    curr = []
                    visited.add((y, x))
                    dfs((y, x), (0, 0))
                    comps.add(tuple(curr))
        
        return len(comps)

        