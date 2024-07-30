class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        length = len(board[0])
        width = len(board)

        top = board[0]
        bottom = board[width - 1]
        left = [board[i][0] for i in range(width)]
        right = [board[i][length - 1] for i in range(width)]

        current = set()
        queue = deque()

        for ind in range(len(top)):
            queue.append((ind, 0))
        for ind in range(len(bottom)):
            queue.append((ind, width - 1))
        for ind in range(len(left)):
            queue.append((0, ind))
        for ind in range(len(right)):
            queue.append((length - 1, ind))

        print(queue)
        while queue:
            x, y = queue.popleft()
            if (x, y) in current or not (x >= 0 and x < length and y >= 0 and y < width) or board[y][x] == "X":
                continue
            current.add((x, y))
            queue.append((x + 1, y))
            queue.append((x - 1, y))
            queue.append((x, y + 1))
            queue.append((x, y - 1))
        print(current)
        for y in range(width):
            for x in range(length):
                if board[y][x] == "O" and (x, y) not in current:
                    board[y][x] = "X"

        return board
        