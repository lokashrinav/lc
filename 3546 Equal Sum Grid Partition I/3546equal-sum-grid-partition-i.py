class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        '''
        1, 4
        2, 3
        '''
        res = []
        for i in range(len(grid)):
            total = 0
            for p in range(len(grid[0])):
                total += grid[i][p]
            res.append(total)

        curr = res[0]
        curr2 = sum(res) - curr
        for i in range(1, len(grid)):
            if curr == curr2:
                return True
            curr += res[i]
            curr2 -= res[i]

        res = []
        for p in range(len(grid[0])):
            total = 0
            for i in range(len(grid)):
                total += grid[i][p]
            res.append(total)

        curr = res[0]
        curr2 = sum(res) - curr
        for i in range(1, len(grid[0])):
            if curr == curr2:
                return True
            curr += res[i]
            curr2 -= res[i]

        return False
            
            
                