from heapq import heappop

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:

        y, x = start
        heap = [(0, y, x)]
        directions = [[-1, 0], [0, 1], [0, -1], [1, 0]]
        visited = {}
        visited[tuple(start)] = 0

        while heap:
            count, y, x = heappop(heap)

            if (y, x) == tuple(destination):
                return count
            
            for i in range(len(directions)):
                y2, x2 = directions[i]
                ny, nx = y, x
                new_count = 0
                while ny + y2 >= 0 and ny + y2 < len(maze) and nx + x2 < len(maze[0]) and nx + x2 >= 0 and maze[ny + y2][nx + x2] == 0:
                    ny += y2
                    nx += x2
                    new_count += 1

                if (ny, nx) not in visited or count + new_count < visited[(ny, nx)]:
                    heappush(heap, (count + new_count, ny, nx))
                    visited[(ny, nx)] = count + new_count
        
        return -1
                        

        