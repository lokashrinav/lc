class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:

        start = None
        count = 0
        for y in range(len(classroom)):
            for x in range(len(classroom[0])):
                if classroom[y][x] == 'S':
                    start = (y, x)
                if classroom[y][x] == 'L':
                    count += 1

        hset = set()
        visited = {}
        visited[(start, tuple(hset))] = energy
        queue = deque([(start, energy, hset)]) 

        dirs = [[0,1], [1, 0], [-1, 0], [0, -1]]

        row = 0
        
        while queue:
            #print(queue)
            for i in range(len(queue)):
                curr, en, hset = queue.popleft()
                y, x = curr

                if len(hset) == count: 
                    return row

                en = energy if classroom[y][x] == 'R' else en

                if en > 0:
                    for ny, nx in dirs:
                        dy, dx = y + ny, x + nx
                        if len(classroom) > dy >= 0 and len(classroom[0]) > dx >= 0 and classroom[dy][dx] != 'X':
                            new_set = hset
                            if classroom[dy][dx] == 'L':
                                new_set = hset | {(dy, dx)}
                            
                            key = ((dy, dx), frozenset(new_set))  
                            if visited.get(key, -1) >= en - 1:
                                continue
                            visited[key] = en - 1
                            
                            queue.append(((dy, dx), en - 1, new_set))
            row += 1
            
        return -1
        

                            