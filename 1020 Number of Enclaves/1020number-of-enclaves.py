class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        enclaved = defaultdict(bool)
        parent = {(y, x):(y, x) for y in range(len(grid)) for x in range(len(grid[0]))}

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    if y == 0 or y == len(grid) - 1 or x == 0 or x == len(grid[0]) - 1:
                        enclaved[(y, x)] = True

        def find(a):
            if a != parent[a]:
                parent[a] = find(parent[a])
            return parent[a]

        def union(a, b):
            first, second = find(a), find(b)
            if first == second:
                return
            
            parent[first] = second
            enclaved[second] = enclaved[first] or enclaved[second]
        
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                for ny, nx in dirs:
                    dy, dx = ny + y, nx + x
                    if len(grid) > dy >= 0 and len(grid[0]) > dx >= 0 and grid[y][x] == 1 and grid[dy][dx] == 1:
                        union((y, x), (dy, dx))
        
        print(enclaved)

        total = 0      
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                ny, nx = find((y, x))
                if grid[y][x] and not enclaved[(ny, nx)]:
                    total += 1
        
        return total
        