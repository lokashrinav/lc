class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # Number of rows and columns in the grid
        num_rows, num_cols = len(grid), len(grid[0])
      
        # Arrays to keep track of the count of servers in each row and column
        rows = [0] * num_rows
        columns = [0] * num_cols
      
        # First pass: count the number of servers in each row and column
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 1:
                    rows[i] += 1
                    columns[j] += 1
      
        # Second pass: count the number of servers that can communicate
        # Servers can communicate if they are in the same row or column with another server
        server_count = 0
        for i in range(num_rows):
            for j in range(num_cols):
                # Check if there's a server and if it's not the only server in its row or column
                if grid[i][j] == 1 and (rows[i] > 1 or columns[j] > 1):
                    server_count += 1
        
        return server_count
      