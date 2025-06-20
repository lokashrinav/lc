class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:

        if len(grid) == 1 and len(grid[0]) == 1:
            return True

        def dfs(curr, d):
            print(curr, d)
            y, x = curr

            if y >= len(grid) or y < 0 or x >= len(grid[0]) or x < 0:
                return False

            if (y, x) in visited:
                return False

            if y == len(grid) - 1 and x == len(grid[0]) - 1:
                return (d == "right" and grid[y][x] in [1, 3, 5]) or (d == "down" and grid[y][x] in [2, 6, 5])
            
            visited.add(curr)

            f = grid[y][x]

            if f == 1 and d == "right":
                return dfs((y, x + 1), "right")
            if f == 1 and d == "left":
                return dfs((y, x - 1), "left")
            if f == 2 and d == "up":
                return dfs((y - 1, x), "up")
            elif f == 2 and d == "down":
                return dfs((y + 1, x), "down")
            elif f == 3 and d == "right":
                return dfs((y + 1, x), "down")
            elif f == 3 and d == "up":
                return dfs((y, x - 1), "left")
            elif f == 4 and d == "up":
                return dfs((y, x + 1), "right")
            elif f == 4 and d == "left":
                return dfs((y + 1, x), "down")
            elif f == 5 and d == "right":
                return dfs((y - 1, x), "up")
            elif f == 5 and d == "down":
                return dfs((y, x - 1), "left")
            elif f == 6 and d == "down":
                return dfs((y, x + 1), "right")
            elif f == 6 and d == "left":
                return dfs((y - 1, x), "up")
            else:
                return False
        
        f = grid[0][0]
        visited = set()
        first = (0, 0)

        if f == 1:
            return dfs(first, "right")
        elif f == 2:
            return dfs(first, "down")
        elif f == 3:
            return dfs(first, "right")
        elif f == 4:
            calc1 = dfs((0, 0), "left") 
            visited = set()
            calc2 = dfs((0, 0), "up")
            return calc1 or calc2
        elif f == 5:
            return False
        elif f == 6:
            return dfs((0, 0), "down")
        
                