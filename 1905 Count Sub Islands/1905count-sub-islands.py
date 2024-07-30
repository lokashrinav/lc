class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def check(node):
            y, x = node
            if not (x >= 0 and x < length and y < width and y >= 0):
                return False
            return True
        length = len(grid2[0])
        width = len(grid2)
        queue = deque()
        visited = set()
        subIslands = 0

        for i in range(width):
            for p in range(length):
                if grid2[i][p] == 0 or (i, p) in visited:
                    continue                
                queue.append((i, p))
                bool1 = True
                while queue:
                    for v in range(len(queue)):
                        y, x = queue.popleft()

                        if (y, x) in visited or grid2[y][x] == 0:
                            continue

                        visited.add((y, x))

                        if grid1[y][x] == 0 and grid2[y][x] == 1:
                            bool1 = False

                        if check((y + 1, x)):
                            queue.append((y + 1, x))
                        if check((y - 1, x)):
                            queue.append((y - 1, x))
                        if check((y, x - 1)):
                            queue.append((y, x - 1))
                        if check((y, x + 1)):
                            queue.append((y, x + 1))
                        
                if bool1 == True:
                    subIslands += 1

        return subIslands

                        


        