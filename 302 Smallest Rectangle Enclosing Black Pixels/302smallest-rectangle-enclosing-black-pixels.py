class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        
        x, y = y, x
        visited = set()
        visited.add((y, x))
        dirs =  [[0, 1], [1, 0], [-1, 0], [0, -1]]
        def dfs(y, x):
            curr = [y, x, y, x]
            for ny, nx in dirs:
                dy, dx = ny + y, nx + x
                if dy >= 0 and dy < len(image) and dx >= 0 and dx < len(image[0]) and (dy, dx) not in visited and image[dy][dx] == "1":
                    visited.add((dy, dx))
                    y1, x1, y2, x2 = dfs(dy, dx)
                    curr[0] = min(y1, curr[0])
                    curr[1] = min(x1, curr[1])
                    curr[2] = max(y2, curr[2])
                    curr[3] = max(x2, curr[3])
                    

            return curr

        y1, x1, y2, x2 = dfs(y, x)

        return (y2 - y1 + 1) * (x2 - x1 + 1)
