class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        for i in range(m):
            for p in range(n):
                if grid[i][p] == 1:
                    queue.append(((i, p), set([(i, p)]), 0))
                    grid[i][p] = -1
                elif grid[i][p] == 2:
                    grid[i][p] = -2

        num_of_build = len(queue)

        hmap = defaultdict(int)

        def idk():
            minNum = []
            while queue:
                for i in range(len(queue)):
                    start, sid, val = queue.popleft()
                    y1, x1 = start   
                    hmap[start] += val

                    if grid[y1][x1] >= 0:
                        grid[y1][x1] += 1

                    if grid[y1][x1] == num_of_build:
                        minNum.append((y1, x1))

                    arr = []
                    for y2, x2 in dirs:
                        y = y1 + y2
                        x = x1 + x2
                        if (y, x) not in sid and y >= 0 and x >= 0 and x < n and y < m and grid[y][x] >= 0:
                            arr.append((y, x))
                    
                    for elem in arr:
                        sid.add(elem)

                    for y, x in arr:
                        queue.append(((y, x), sid, val + 1))
            
            fun = float('inf')
            saved = None
            for y, x in minNum:
                if hmap[(y, x)] < fun:
                    saved = (y, x)
                    fun = hmap[(y, x)]

            return fun if fun != float('inf') else None

        minNum = idk()

        print(hmap)

        if minNum is None:
            return -1
        
        return minNum








        '''fin_y, fin_x = minNum

        queue = deque()

        for i in range(m):
            for p in range(n):
                if grid[i][p] == -1:
                    queue.append(((i, p), set(), 0))

        total = 0
        while queue:
            for i in range(len(queue)):
                start, sid, val = queue.popleft()
                y1, x1 = start     

                if y1 == fin_y and x1 == fin_x:
                    total += val
                    continue

                arr = []
                for y2, x2 in dirs:
                    y = y1 + y2
                    x = x1 + x2
                    if (y, x) not in sid and y >= 0 and x >= 0 and x < n and y < m and grid[y][x] >= 0:
                        arr.append((y, x))
                
                for elem in arr:
                    sid.add(elem)

                for y, x in arr:
                    queue.append(((y, x), sid, val + 1))
        
        return minTotal'''