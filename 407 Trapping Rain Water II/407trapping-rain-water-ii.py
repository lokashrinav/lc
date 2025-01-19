from heapq import heappop, heappush 

class Solution:
    def trapRainWater(self, height_map: List[List[int]]) -> int:
        # Get the dimensions of the map
        rows, cols = len(height_map), len(height_map[0])
      
        # Initialize a 2D visited array to keep track of processed cells
        visited = [[False] * cols for _ in range(rows)]
      
        # Priority Queue (min heap) to process the cells by height
        min_heap = []
      
        # Initialize the heap with the boundary cells and mark them as visited
        for i in range(rows):
            for j in range(cols):
                if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                    heappush(min_heap, (height_map[i][j], i, j))
                    visited[i][j] = True
      
        # Total amount of trapped water
        trapped_water = 0
      
        # Directions for neighboring cells
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
      
        # Process the cells until the heap is empty
        while min_heap:
            height, x, y = heappop(min_heap)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # Check if the neighbor is within bounds and not visited
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                    # Calculate the possible water level difference
                    trapped_water += max(0, height - height_map[nx][ny])
                  
                    # Mark the neighbor as visited
                    visited[nx][ny] = True
                  
                    # Push the neighbor cell onto the heap with the max height
                    # to keep track of the 'water surface' level
                    heappush(min_heap, (max(height, height_map[nx][ny]), nx, ny))
      
        # Return the total accumulated trapped water
        return trapped_water