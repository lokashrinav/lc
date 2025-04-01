class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rect = rectangle
        self.arr = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.arr.append(((col1, row1), (col2, row2), newValue))

    def getValue(self, row: int, col: int) -> int:
        change = self.rect[row][col]
        for i in range(len(self.arr)):
            p1, p2, val = self.arr[i]
            x1, y1 = p1
            x2, y2 = p2
            if x1 <= col <= x2 and y1 <= row <= y2:
                change = val
        return change

            
        


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)