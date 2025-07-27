class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        queue = deque([[0, 0]])
        count = 0
        dirs = [[2, 1], [1, 2], [-1, 2], [1, -2], [-1, -2], [-2, -1], [2, -1], [-2, 1]]
        visited = set()

        while queue:
            for i in range(len(queue)):
                dy, dx = queue.popleft()
                if dy == y and dx == x:
                    return count
                for ny, nx in dirs:
                    ry, rx = dy + ny, nx + dx
                    if (ry, rx) in visited:
                        continue
                    queue.append((ry, rx))
                    visited.add((ry, rx))

            count += 1
        

        