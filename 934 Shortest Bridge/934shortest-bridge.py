class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        curr = None
        for i in range(m):
            for p in range(n):
                if grid[i][p] == 1:
                    curr = (i, p)
                    break

        queue = deque()

        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def dfs(curr):
            y, x = curr
            queue.append((y, x))
            grid[y][x] = 2
            
            for y2, x2 in directions:
                ny, nx = y + y2, x + x2
                if ny >= 0 and nx >= 0 and ny < m and nx < n and grid[ny][nx] == 1:
                    dfs((ny, nx))
                    grid[ny][nx] = 2
            
        
        dfs(curr)
        #print(queue)

        level = 0
        while queue:
            for i in range(len(queue)):
                y, x = queue.popleft()
                # print((y, x), grid[y][x], end=' ')

                if grid[y][x] == 1:
                    return level - 1

                if grid[y][x] == 0:
                    grid[y][x] = -1

                for y2, x2 in directions:
                    ny, nx = y + y2, x + x2
                    if ny >= 0 and nx >= 0 and ny < m and nx < n and (grid[ny][nx] == 0 or grid[ny][nx] == 1):
                        queue.append((ny, nx))
                        if grid[ny][x] == 0:
                            grid[ny][nx] = -1

            level += 1

        # print('hi')

        return level




        