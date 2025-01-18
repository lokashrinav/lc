class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        queue = []
        queue.append((0, 0, 0))
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = {(0, 0): 0}
        while queue:
            count, y, x = heapq.heappop(queue)

            if (y, x) in visited and visited[(y, x)] < count:
                continue

            if y == len(grid) - 1 and x == len(grid[0]) - 1:
                return count

            num = grid[y][x]

            for i in range(len(directions)):
                ny, nx = y + directions[i][0], x + directions[i][1] 
                currCount = count + 1 if i != num - 1 else count
                if ny >= 0 and nx >= 0 and nx < len(grid[0]) and ny < len(grid) and ((ny, nx) not in visited or (visited[(ny, nx)] > currCount)):
                    if i != num - 1:
                        heapq.heappush(queue, (currCount, ny, nx))
                    else:
                        heapq.heappush(queue, (currCount, ny, nx))
                    
                
                    visited[(ny, nx)] = currCount

        return 0
            


    