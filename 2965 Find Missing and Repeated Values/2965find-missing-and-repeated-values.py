class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])

        ans = [None, None]
        visited = set()
        for i in range(m):
            for p in range(n):
                if grid[i][p] in visited:
                    ans[0] = grid[i][p]

                visited.add(grid[i][p])   

        for i in range(1, m * n + 1):
            if i not in visited:
                ans[1] = i
                break
        
        return ans

