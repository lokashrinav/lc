class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        

        queue = deque()
        visited = set()

        for i in range(len(mat)):
            for p in range(len(mat[0])):
                if mat[i][p] == 0:
                    queue.append((i, p))
                    visited.add((i, p))

        level = 0
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        while queue:
            for i in range(len(queue)):
                y2, x2 = queue.popleft()
                mat[y2][x2] = level
                
                for y, x in directions:
                    ny, nx = y + y2, x2 + x
                    if ny >= 0 and nx >= 0 and nx < len(mat[0]) and ny < len(mat) and (ny, nx) not in visited:
                        queue.append((ny, nx))
                        visited.add((ny, nx))
            level += 1
        
        return mat
