from typing import List
import math

class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        """
        LeetCode 1515: Best Position for a Service Centre
        Using Weiszfeld's algorithm to find geometric median
        """

        def total(x, y):
            tot = 0
            for px, py in positions:
                tot += math.sqrt((px - x) ** 2 + (py - y) ** 2)
            return tot
        
        positions = [(float(y), float(x)) for y, x in positions]

        y, x = sum(y for x, y in positions) / len(positions), sum(x for x, y in positions) / len(positions)

        for i in range(1000):
            numx = numy = den = 0

            for px, py in positions:
                dist = math.sqrt((px - x) ** 2 + (py - y) ** 2)
                if dist < 1e-12:
                    continue
                
                w = 1 / dist
                numy += py * w
                numx += px * w
                den += w
            
            if den == 0:
                break

            ny, nx = numy / den, numx / den

            if math.sqrt((x - nx) ** 2 + (y - ny) ** 2) < 1e-12:
                break

            x, y = nx, ny

        return total(x, y)