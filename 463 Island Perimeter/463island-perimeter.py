class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        '''
        1 -> 4 = 4
        2 -> 3 + 3 = 6
        3 -> 3 + 2 + 3 = 8
        4 -> 3 + 2 + 2 + 3 = 10
        '''

        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visited = set()
        def dfs(y, x):
            
            curr = 4
            for ny, nx in dirs:
                dy, dx = ny + y, nx + x
                if len(grid) > dy >= 0 and len(grid[0]) > dx >= 0 and grid[dy][dx] == 1:
                    curr -= 1
            
            for ny, nx in dirs:
                dy, dx = ny + y, nx + x
                if (dy, dx) not in visited and len(grid) > dy >= 0 and len(grid[0]) > dx >= 0 and grid[dy][dx] == 1:
                    visited.add((dy, dx))
                    curr += dfs(dy, dx)
            
            return curr
                    
        total = 0 
        for i in range(len(grid)):
            for p in range(len(grid[0])):
                if (i, p) in visited or grid[i][p] == 0:
                    continue
                visited.add((i, p))
                total += dfs(i, p)
        
        return total
        