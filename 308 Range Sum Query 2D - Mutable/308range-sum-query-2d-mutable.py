class NumMatrix:

    def build_y(self, noder, rlx, rrx, nodec, clx, clrx):
        if clx == clrx:
            if rlx == rrx:
                self.tree[noder][nodec] = self.matrix[rlx][clx]
            else:
                self.tree[noder][nodec] = self.tree[noder * 2][nodec] + self.tree[noder * 2 + 1][nodec]
        else:
            mid = (clx + clrx) // 2
            self.build_y(noder, rlx, rrx, nodec * 2, clx, mid)
            self.build_y(noder, rlx, rrx, nodec * 2 + 1, mid + 1, clrx)
            self.tree[noder][nodec] = self.tree[noder][nodec * 2] + self.tree[noder][nodec * 2 + 1]

    def __init__(self, matrix: List[List[int]]):
        self.tree = [[0 for i in range(len(matrix[0]) * 4)] for p in range(len(matrix) * 4)]
        self.matrix = matrix
        self.m, self.n = len(matrix), len(matrix[0])
        self.build_x(1, 0, self.m - 1)

    def build_x(self, nodex, lx, rx):
        if lx != rx:
            mid = (lx + rx) // 2
            self.build_x(nodex * 2, lx, mid)
            self.build_x(nodex * 2 + 1, mid + 1, rx)
        self.build_y(nodex, lx, rx, 1, 0, self.n - 1)

    def query_y(self, node, col_node, col_start, col_end, cstart, cend):
        if col_start > cend or cstart > col_end:
            return 0
        if col_start >= cstart and col_end <= cend:
            return self.tree[node][col_node]
        mid = (col_start + col_end) // 2
        return self.query_y(node, col_node * 2, col_start, mid, cstart, cend) + self.query_y(node, col_node * 2 + 1, mid + 1, col_end, cstart, cend)
    
    def query_x(self, node, row_start, row_end, rstart, rend, cstart, cend):
        if row_start > rend or rstart > row_end:
            return 0
        if row_start >= rstart and row_end <= rend:
            return self.query_y(node, 1, 0, self.n - 1, cstart, cend)
        
        mid = (row_start + row_end) // 2
        return self.query_x(node * 2, row_start, mid, rstart, rend, cstart, cend) + self.query_x(node * 2 + 1, mid + 1, row_end, rstart, rend, cstart, cend)

    def update_y(self, node, row_start, row_end, col_node, col_start, col_end, row, col, val):
        if col_start == col_end:
            if row_start == row_end:
                self.tree[node][col_node] = val
            else:
                self.tree[node][col_node] = self.tree[node * 2][col_node] + self.tree[node * 2 + 1][col_node]
        else:
            mid = (col_end + col_start) // 2
            if col <= mid:
                self.update_y(node, row_start, row_end, col_node * 2, col_start, mid, row, col, val)
            else:
                self.update_y(node, row_start, row_end, col_node * 2 + 1, mid + 1, col_end, row, col, val)
            
            self.tree[node][col_node] = self.tree[node][col_node * 2] + self.tree[node][col_node * 2 + 1] 

    def update_x(self, node, row_start, row_end, row, col, val):
        if row_start != row_end:
            mid = (row_start + row_end) // 2
            if row <= mid:
                self.update_x(node * 2, row_start, mid, row, col, val)
            else:
                self.update_x(node * 2 + 1, mid + 1, row_end, row, col, val)

        self.update_y(node, row_start, row_end, 1, 0, self.n - 1, row, col, val)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.query_x(1, 0, self.m - 1, row1, row2, col1, col2)

    def update(self, row: int, col: int, val: int) -> None:
        self.matrix[row][col] = val
        self.update_x(1, 0, self.m - 1, row, col, val)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)