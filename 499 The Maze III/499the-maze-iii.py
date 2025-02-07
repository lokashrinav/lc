class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        
        y, x = ball
        heap = [(0, [], y, x, 0)]
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        op = {(0, 1):'r', (1, 0):'d', (-1, 0):'u', (0, -1):'l'}
        visited = set()

        while heap:
            print(heap)
            count, curr, y, x, idk = heappop(heap)
            visited.add((y, x))
            if idk:
                return ''.join(curr)

            for dy, dx in directions:
                cy, cx = y, x
                new_count = 0
                while cy + dy < len(maze) and cx + dx < len(maze[0]) and cy + dy >= 0 and cx + dx >= 0 and maze[cy + dy][cx + dx] == 0:
                    new_count += 1
                    cy += dy
                    cx += dx
                    if (cy, cx) == tuple(hole):
                        idk = 1
                        break
            
                if (cy, cx) not in visited:
                    heappush(heap, (count + new_count, curr + [op[(dy, dx)]], cy, cx, idk))
                if idk:
                    idk = 0
        return "impossible"

''' [0,0,1,0,0],
    [0,0,0,0,0],
    [0,0,0,1,0],
    [1,1,0,1,1],
    [0,0,0,0,0]


        return "impossible"
        '''