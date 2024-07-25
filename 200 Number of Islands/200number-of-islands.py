class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        queue = deque()
        length = len(grid[0])
        width = len(grid)
        visited = set()
        num_of_islands = 0

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                dist = 0
                queue.append((x, y))
                while queue:
                    for i in range(len(queue)):
                        a, b = queue.popleft()
                        if (a, b) in visited or (a < 0 or a >= length or b < 0 or b >= width) or grid[b][a] == "0":
                            continue
                        visited.add((a, b))
                        queue.append((a + 1, b))
                        queue.append((a - 1, b))
                        queue.append((a, b + 1))
                        queue.append((a, b - 1))
                        dist = 1
                num_of_islands += dist
        return num_of_islands                
                
                
                
        