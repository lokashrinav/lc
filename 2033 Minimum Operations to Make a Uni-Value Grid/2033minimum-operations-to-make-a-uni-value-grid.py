class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:

        prev = None

        arr = []

        num1 = x

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if prev and (abs(prev - grid[y][x]) % num1 != 0):
                    return -1
                prev = grid[y][x]

                arr.append(grid[y][x])
        
        arr.sort()

        num = arr[len(arr) // 2]

        total = 0

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                diff = abs(grid[y][x] - num)
                total += (diff // num1)
        
        return total

        

        