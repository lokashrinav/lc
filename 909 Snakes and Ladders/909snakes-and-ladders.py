from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # Helper function to map the board number to board coordinates (i,j)
        def get_square_coordinates(square_number):
            row, col = (square_number - 1) // board_size, (square_number - 1) % board_size
            if row % 2 == 1:
                # On odd rows, the counting is from right to left.
                col = board_size - 1 - col
            # Transform row to start from bottom of board
            return board_size - 1 - row, col

        board_size = len(board)  # n by n board
        queue = deque([1])  # Start from square 1
        visited = {1}  # Keep track of visited squares
        steps = 0  # Counter for number of moves

        while queue:
            # Process all squares at the current depth.
            for _ in range(len(queue)):
                current_square = queue.popleft()

                # Win condition: reached the last square
                if current_square == board_size * board_size:
                    return steps

                # Check all possible next moves by dice roll (1-6)
                for next_square in range(current_square + 1, min(current_square + 7, board_size * board_size + 1)):
                    i, j = get_square_coordinates(next_square)

                    # If there's a ladder or snake, take it.
                    if board[i][j] != -1:
                        next_square = board[i][j]

                    # If next square has not been visited, add it to the queue
                    if next_square not in visited:
                        queue.append(next_square)
                        visited.add(next_square)

            # Increment the number of moves after expanding all possible moves at current depth.
            steps += 1
      
        # If we have exited the loop without reaching the last square, it's not possible to win.
        return -1