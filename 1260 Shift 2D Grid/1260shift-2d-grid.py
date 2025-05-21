class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        res = []
        for i in range(len(grid)):
            for p in range(len(grid[0])):
                res.append(grid[i][p])
        
        graph = [[0] * len(grid[0]) for i in range(len(grid))]

        k = k % len(res)

        for i in range(len(res)):
            ind = len(res) - ((k - i - 1) % len(res)) - 1
            print(len(res) - ((k - i - 1) % len(res)) - 1)
            print(i // len(grid), i % len(grid))
            graph[i // len(grid[0])][i % len(grid[0])] = res[ind]
        
        return graph
        