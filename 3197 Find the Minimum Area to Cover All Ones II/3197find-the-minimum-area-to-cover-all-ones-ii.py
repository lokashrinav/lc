from typing import List
from math import inf

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        # Function to calculate the area of the rectangle covering all 1s in given subgrid
        def f(i1: int, j1: int, i2: int, j2: int) -> int:
            x1 = y1 = inf  # Initialize top-left corner as infinity
            x2 = y2 = -inf # Initialize bottom-right corner as negative infinity
            for i in range(i1, i2 + 1): # Traverse through rows in the subgrid
                for j in range(j1, j2 + 1): # Traverse through columns in the subgrid
                    if grid[i][j] == 1: # Check if the current cell contains 1
                        x1 = min(x1, i) # Update the top-most row containing 1
                        y1 = min(y1, j) # Update the left-most column containing 1
                        x2 = max(x2, i) # Update the bottom-most row containing 1
                        y2 = max(y2, j) # Update the right-most column containing 1
            # Calculate the area of the rectangle covering all 1s
            return (x2 - x1 + 1) * (y2 - y1 + 1)

        m, n = len(grid), len(grid[0]) # Get dimensions of the grid
        ans = m * n # Start with maximum possible area (entire grid)
      
        # Case 1: Split the grid horizontally into three parts
        for i1 in range(m - 1):
            for i2 in range(i1 + 1, m - 1):
                ans = min(
                    ans,
                    f(0, 0, i1, n - 1)               # Area of first part
                    + f(i1 + 1, 0, i2, n - 1)       # Area of second part
                    + f(i2 + 1, 0, m - 1, n - 1)    # Area of third part
                )
      
        # Case 2: Split the grid vertically into three parts
        for j1 in range(n - 1):
            for j2 in range(j1 + 1, n - 1):
                ans = min(
                    ans,
                    f(0, 0, m - 1, j1)               # Area of first part
                    + f(0, j1 + 1, m - 1, j2)       # Area of second part
                    + f(0, j2 + 1, m - 1, n - 1)    # Area of third part
                )
      
        # Case 3: Split the grid in other possible shapes
        for i in range(m - 1):
            for j in range(n - 1):
                ans = min(
                    ans,
                    f(0, 0, i, j)                   # Area of first part
                    + f(0, j + 1, i, n - 1)         # Area of second part
                    + f(i + 1, 0, m - 1, n - 1)    # Area of third part
                )
                ans = min(
                    ans,
                    f(0, 0, i, n - 1)               # Area of first part
                    + f(i + 1, 0, m - 1, j)        # Area of second part
                    + f(i + 1, j + 1, m - 1, n - 1) # Area of third part
                )
                ans = min(
                    ans,
                    f(0, 0, i, j)                   # Area of first part
                    + f(i + 1, 0, m - 1, j)        # Area of second part
                    + f(0, j + 1, m - 1, n - 1)    # Area of third part
                )
                ans = min(
                    ans,
                    f(0, 0, m - 1, j)               # Area of first part
                    + f(0, j + 1, i, n - 1)        # Area of second part
                    + f(i + 1, j + 1, m - 1, n - 1) # Area of third part
                )
      
        return ans