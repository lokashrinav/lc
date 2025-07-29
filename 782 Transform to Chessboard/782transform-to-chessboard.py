class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)

        first_row = board[0]
        complement_row = [1 - x for x in first_row]
        hmap = defaultdict(int)

        for row in board:
            hmap[tuple(row)] += 1

        if len(hmap) != 2 or tuple(first_row) not in hmap and tuple(complement_row) not in hmap:
            return -1

        keys = list(hmap.keys())

        if len(board) % 2 == 1:
            if abs(hmap[keys[0]] - hmap[keys[1]]) != 1:
                return -1
        else:
            if abs(hmap[keys[0]] - hmap[keys[1]]) != 0:
                return -1    

        first_col = [board[i][0] for i in range(n)]
        complement_col = [1 - x for x in first_col]
        hmap_col = defaultdict(int)

        for j in range(n):
            col = tuple(board[i][j] for i in range(n))
            hmap_col[col] += 1

        if len(hmap_col) != 2 or tuple(first_col) not in hmap_col or tuple(complement_col) not in hmap_col:
            return -1

        col_keys = list(hmap_col.keys())

        if n % 2 == 1:
            if abs(hmap_col[col_keys[0]] - hmap_col[col_keys[1]]) != 1:
                return -1
        else:
            if abs(hmap_col[col_keys[0]] - hmap_col[col_keys[1]]) != 0:
                return -1

        mat = []
        for i in range(len(board)):
            mat.append(board[0][i])

        count = 0
        for i in range(len(mat)):
            curr = i % 2
            if mat[i] != curr:
                count += 1

        count2 = 0
        for i in range(len(mat)):
            curr = not (i % 2)
            if mat[i] != curr:
                count2 += 1

        fun1 = float('inf')
        if count % 2 == 0:
            fun1 = count // 2
        if count2 % 2 == 0:
            fun1 = min(fun1, count2 // 2)

        mat = []
        for i in range(len(board)):
            mat.append(board[i][0])

        count = 0
        for i in range(len(mat)):
            curr = i % 2
            if mat[i] != curr:
                count += 1

        count2 = 0
        for i in range(len(mat)):
            curr = not (i % 2)
            if mat[i] != curr:
                count2 += 1

        #print(mat, count, count2)    
        fun2 = float('inf')
        if count % 2 == 0:
            fun2 = count // 2
        if count2 % 2 == 0:
            fun2 = min(fun2, count2 // 2)

        return fun1 + fun2