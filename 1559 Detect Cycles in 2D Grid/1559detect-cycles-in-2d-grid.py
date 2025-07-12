class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:

        visited = set()
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def dfs(ind, prev):
            y, x = ind
            if ind in visited:
                return True
            visited.add(ind)

            for ny, nx in dirs:
                dy, dx = ny + y, nx + x
                if (dy, dx) != prev and len(grid) > dy >= 0 and len(grid[0]) > dx >= 0 and grid[dy][dx] == grid[y][x]:
                    if dfs((dy, dx), ind):
                        return True
            return False

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if (y, x) not in visited:
                    if dfs((y, x), None):
                        return True
        
        return False

        