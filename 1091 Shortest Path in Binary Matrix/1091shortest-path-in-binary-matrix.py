class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]:
            return -1

        queue = deque()
        queue.append((0, 0))

        visited = set()
        count = 0

        direct = [[-1, -1], [0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [-1, 1], [1, -1]]

        while queue:
            count += 1
            for i in range(len(queue)):
                y, x = queue.popleft()
                visited.add((y, x))
                if y == len(grid) - 1 and x == len(grid) - 1:
                    return count

                for y1, x1 in direct:
                    ny, nx = y1 + y, x1 + x
                    if ny >= 0 and ny < len(grid) and nx < len(grid) and nx >= 0 and (ny, nx) not in visited and grid[ny][nx] == 0:
                        queue.append((ny, nx))
                        visited.add((ny, nx))

        return -1

