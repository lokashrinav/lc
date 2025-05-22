class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:

        
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        def dfs(y, x, c):
            for ny, nx in dirs:
                dy, dx = y + ny, x + nx
                if  (dy, dx) not in curr and len(grid) > dy >= 0 and len(grid[0]) > dx >= 0 and grid[dy][dx] == c:
                    curr.add((dy, dx))
                    dfs(dy, dx, c)
        
        def border(y, x, c):
            for ny, nx in dirs:
                dy, dx = y + ny, x + nx
                if (dy, dx) in curr:
                    continue
                if len(grid) > dy >= 0 and len(grid[0]) > dx >= 0 and grid[dy][dx] == c:
                    curr.add((dy, dx))
                    border(dy, dx, c)
                else:
                    grid[y][x] = color
        
        visited = set()
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if (y, x) in visited:
                    continue
                
                curr = set()
                curr.add((y, x))

                dfs(y, x, grid[y][x])

                visited.update(curr)

                if (row, col) in curr:
                    curr = set()
                    curr.add((y, x))
                    border(y, x, grid[y][x])
        
        return grid

                
        