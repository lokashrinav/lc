class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def connected(y, x):
            if (y, x) in visited:
                return

            visited.add((y, x))
            for ny, nx in dirs:
                dy, dx = ny + y, nx + x
                if len(grid) > dy >= 0 and len(grid[0]) > dx >= 0 and grid[dy][dx] > 0:
                    connected(dy, dx)

        def dfs(y, x):

            total = saved = grid[y][x]

            grid[y][x] = 0

            for ny, nx in dirs:
                dy, dx = ny + y, nx + x
                if len(grid) > dy >= 0 and len(grid[0]) > dx >= 0 and grid[dy][dx] > 0:
                    total = max(total, saved + dfs(dy, dx))

            grid[y][x] = saved

            return total

        total = 0
        final = set()
        hmap = defaultdict(int)
        for i in range(len(grid)):
            for p in range(len(grid[0])):
                if (i, p) in final or grid[i][p] == 0:
                    continue
                visited = set()
                connected(i, p)
                final.update(visited)
                idk = 0

                for y, x in visited:
                    idk = max(dfs(y, x), idk)

                total = max(idk, total)

        return total