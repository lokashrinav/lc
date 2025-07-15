class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue = deque()
        total = 0

        for i in range(len(grid)):
            for p in range(len(grid[0])):
                if grid[i][p] == 2:
                    queue.append((i, p))
                elif grid[i][p] == 1:
                    total += 1

        if total == 0:
            return 0

        if not queue:
            return -1
        
        levels = 0
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        while queue:
            for i in range(len(queue)):
                ny, nx = queue.popleft()
                for y, x in dirs:
                    dy, dx = ny + y, nx + x
                    if len(grid) > dy >= 0 and len(grid[0]) > dx >= 0 and grid[dy][dx] == 1:
                        grid[dy][dx] = 2
                        total -= 1
                        queue.append((dy, dx))
                        if total == 0:
                            return levels + 1
            levels += 1

        for i in range(len(grid)):
            for p in range(len(grid[0])):
                if grid[i][p] == 1:
                    return -1
        
        return levels