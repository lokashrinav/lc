class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:

        hmap = {}

        for i in range(len(mat)):
            for p in range(len(mat[0])):
                hmap[mat[i][p]] = (i, p)

        row_count = [0] * len(mat)
        col_count = [0] * len(mat[0])

        for i in range(len(arr)):
            y, x = hmap[arr[i]]
            row_count[y] += 1
            col_count[x] += 1

            if row_count[y] == len(mat[0]) or col_count[x] == len(mat):
                return i
        



        