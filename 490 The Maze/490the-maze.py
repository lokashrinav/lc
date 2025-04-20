class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        queue = deque([tuple(start)])
        visited = set()

        while queue:
            out = queue.popleft()
            if out in visited:
                continue
            visited.add(out)

            if out == tuple(destination):
                return True
            y, x = out

            for ny, nx in dirs:
                dy, dx = y + ny, nx + x
                prev = None
                while len(maze) > dy >= 0 and len(maze[0]) > dx >= 0 and maze[dy][dx] == 0:
                    prev = (dy, dx)
                    dy, dx = dy + ny, dx + nx

                if prev:
                    queue.append(prev)
        
        return False


                
