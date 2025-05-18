class Solution:
    def minMoves(self, matrix: List[str]) -> int:

        queue = deque()
        queue.append((0, 0))
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        hmap = defaultdict(list)
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x].isalpha():
                    hmap[matrix[y][x]].append((y, x))

        #print(hmap)

        row = 0
        visited = set()
        while queue:
            #print(queue)
            i = 0
            
            for i in range(len(queue)):
                y, x = queue[i]
                if matrix[y][x] in hmap:
                    for elem in hmap[matrix[y][x]]:
                        if elem not in visited:
                            visited.add(elem)
                            queue.append(elem)
            
            for i in range(len(queue)):
                
                y, x = queue.popleft()
                    
                if y == len(matrix) - 1 and x == len(matrix[0]) - 1:
                    return row

                for ny, nx in dirs:
                    dy, dx = ny + y, nx + x
                    if ((dy, dx) not in visited and len(matrix) > dy >= 0 and len(matrix[0]) > dx >= 0 and matrix[dy][dx] != "#"):
                        visited.add((dy, dx))
                        queue.append((dy, dx))
                        
                i += 1
                    
            row += 1

        return -1
            
        