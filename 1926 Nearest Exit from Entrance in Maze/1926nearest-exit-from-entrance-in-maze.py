class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        queue = deque([entrance])
        visited = set()
        visited.add((entrance[0], entrance[1]))
        count = 0
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        while queue:
            for i in range(len(queue)):
                y, x = queue.popleft()
                if y == len(maze) - 1 or x == len(maze[0]) - 1 or y == 0 or x == 0:
                    if [y, x] != entrance:
                        return count
                
                for ny, nx in dirs:
                    dy, dx = ny + y, nx + x
                    if dy >= 0 and dy < len(maze) and dx >= 0 and dx < len(maze[0]) and (dy, dx) not in visited and maze[dy][dx] == ".":
                        visited.add((dy, dx))
                        queue.append((dy, dx))

            count += 1

        return -1
        