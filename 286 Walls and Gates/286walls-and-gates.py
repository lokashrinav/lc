class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        queue = deque()
        m = len(rooms)
        n = len(rooms[0])
        
        for i in range(m):
            for p in range(n):
                if rooms[i][p] == 0:
                    queue.append((i, p))
        
        level = 0
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        while queue:
            for i in range(len(queue)):
                y, x = queue.popleft()
                if rooms[y][x] > 0 and rooms[y][x] != 2147483647:
                    continue

                rooms[y][x] = level
                for i in range(len(directions)):
                    ny, nx = y + directions[i][0], x + directions[i][1]
                    if ny >= 0 and ny < m and nx < n and nx >= 0 and rooms[ny][nx] == 2147483647:
                        queue.append((ny, nx))
            level += 1
        
        return rooms


        