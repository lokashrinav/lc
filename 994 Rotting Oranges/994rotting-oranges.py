class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        length = len(grid[0])
        width = len(grid)
        visited = set()
        queue = deque()
        fresh_oranges = 0
        for y in range(width):
            for x in range(length):
                if grid[y][x] == 2:
                    queue.append((x, y))
                if grid[y][x] == 1:
                    fresh_oranges += 1
        
        if not queue and fresh_oranges > 0:
            return -1

        dist = 0

        while queue:
            for i in range(len(queue)):
                x, y = queue.popleft()
                if (x, y) in visited or not (x >= 0 and x < length and y >= 0 and y < width) or grid[y][x] == 0:
                    continue
                if grid[y][x] == 1:
                    fresh_oranges -= 1
                visited.add((x, y))
                queue.append((x + 1, y))
                queue.append((x - 1, y))
                queue.append((x, y + 1))
                queue.append((x, y - 1))
                if fresh_oranges == 0:
                    return dist
            dist += 1
        if fresh_oranges > 0:
            return -1
        return dist