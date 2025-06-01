class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:

        def func(y, x):
            hmap = defaultdict(int)
            for i in range(y, y + 2):
                for p in range(x, x + 2):
                    hmap[grid[i][p]] += 1
            
            for key, val in hmap.items():
                if val >= 3:
                    return True
            
            return False



        for i in range(len(grid) - 1):
            for p in range(len(grid[0]) - 1):
                if func(i, p):
                    return True
        
        return False

        