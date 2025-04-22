class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:

            y, x = squirrel
            zy, zx = tree
            nuz = set()

            for ny, nx in nuts:
                nuz.add((ny, nx))
            
            memo = {}
            for ny, nx in nuts:
                memo[(ny, nx)] = 2 * (abs(zy - ny) + abs(zx - nx))
            
            sum1 = sum(val for val in memo.values())

            new_set = nuz.copy()
            minNum = float('inf')
            for ny, nx in new_set:
                nuz.remove((ny, nx))
                total_dist = sum1 - memo[(ny, nx)]

                total_dist += abs(ny - y) + abs(nx - x)
                total_dist += abs(ny - zy) + abs(nx - zx)

                nuz.add((ny, nx))

                minNum = min(minNum, total_dist)

            return minNum

                
