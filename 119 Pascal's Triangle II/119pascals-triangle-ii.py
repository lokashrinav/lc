class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]

        for i in range(rowIndex):
            for p in range(i, 0, -1):
                row[p] = row[p] + row[p - 1]

            row.append(1)

        return row