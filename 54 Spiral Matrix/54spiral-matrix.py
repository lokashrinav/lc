class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        visited = set()
        order = []
        dir1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(index, i):
            y, x = index
            
            if index in visited or not (x >= 0 and x < len(matrix[0]) and y < len(matrix) and y >= 0):
                return False

            visited.add((y, x))
            order.append(matrix[y][x])

            i = i % 4
            b, a = dir1[i]

            if dfs((y + b, x + a), i) == False:
                i = (i + 1) % 4
                b, a = dir1[i]
                if dfs((y + b, x + a), i) == False:
                    i = (i + 1) % 4
                    b, a = dir1[i]
                    if dfs((y + b, x + a), i) == False:
                        i = (i + 1) % 4
                        b, a = dir1[i]
                        if dfs((y + b, x + a), i) == False:
                            return True
            return True
                                
                
        
        dfs((0, 0), 0)
        print(order)
        return order

        