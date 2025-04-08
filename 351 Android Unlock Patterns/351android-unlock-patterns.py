class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        def dfs(curr):
            # print(visited)
            if len(visited) > n:
                return 0
            
            y1, x1 = curr

            if len(visited) >= m and len(visited) <= n:
                total = 1
            else:
                total = 0

            for y in range(3):
                for x in range(3):
                    if (abs(y - y1) == 2 and abs(x - x1) == 2) or (abs(y - y1) == 2 and abs(x - x1) == 0 and (y == 1 or x == 1)) or (abs(y - y1) == 0 and abs(x - x1) == 2 and (y == 1 or x == 1)):
                        if (1, 1) in visited and (y, x) not in visited:
                            visited.add((y, x))
                            total += dfs((y, x))
                            visited.remove((y, x))
                    elif (abs(y - y1) == 2 and abs(x - x1) == 0) or (abs(y1 - y) == 0 and abs(x - x1) == 2):
                        if ((y1 + y) // 2, (x1 + x) // 2) in visited and (y, x) not in visited:
                            visited.add((y, x))
                            total += dfs((y, x))
                            visited.remove((y, x))
                    else:
                        if (y, x) not in visited:
                            visited.add((y, x))
                            total += dfs((y, x))
                            visited.remove((y, x))
            
            return total
            
        total = 0
        for y in range(3):
            for x in range(3):
                visited = set([(y, x)])
                calc = dfs((y, x))
                total += calc

        return total

        