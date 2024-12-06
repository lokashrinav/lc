class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        queue = deque()

        for i in range(len(grid)):
            for p in range(len(grid[0])):
                if grid[i][p] == 1:
                    queue.append([i, p])
        
        direct = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        res = -1
        while queue:
            y, x = queue.popleft()

            res = grid[y][x]                

            for fir, sec in direct:
                if min(y + fir, x + sec) >= 0 and max(y + fir, x + sec) < len(grid) and grid[y + fir][x + sec] == 0:
                    queue.append([y + fir, x + sec])
                    grid[y + fir][x + sec] = res + 1
        
        return res - 1 if res > 1 else -1

                
        