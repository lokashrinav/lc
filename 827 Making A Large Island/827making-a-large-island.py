class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        parents = {}

        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]

        def union(first, second):
            idk1 = find(first)
            idk2 = find(second)

            if idk1 != idk2:
                y1, x1 = idk1
                y2, x2 = idk2
                if grid[y1][x1] >= grid[y2][x2]:
                    parents[idk2] = idk1
                    grid[y1][x1] += grid[y2][x2]                 
                elif grid[y1][x1] < grid[y2][x2]:
                    parents[idk1] = idk2
                    grid[y2][x2] += grid[y1][x1] 
            return             
        
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        for i in range(n):
            for p in range(n):
                if (i, p) not in parents:
                    parents[(i, p)] = (i, p)
                if grid[i][p] == 0:
                    continue
                for y, x in directions:
                    ny, nx = i + y, p + x
                    if ny >= 0 and ny < n and nx >= 0 and nx < n and grid[ny][nx] >= 1:
                        if (ny, nx) not in parents:
                            parents[(ny, nx)] = (ny, nx)
                        union((i, p), (ny, nx))
        
        maxNum = max([max(arr) for arr in grid])

        #print(grid)

        #print(parents)

        for i in range(n):
            for p in range(n):
                if grid[i][p] == 0:
                    total = 1
                    hset = set()
                    for y, x in directions:
                        ny, nx = i + y, p + x
                        if ny >= 0 and ny < n and nx >= 0 and nx < n:
                            fun1, fun2 = find((ny, nx))
                            #print((fun1, fun2))
                            if (fun1, fun2) not in hset:
                                total += grid[fun1][fun2]   
                                hset.add((fun1, fun2))
                    #print(hset)
                    maxNum = max(total, maxNum) 
    
        return maxNum
            
                

