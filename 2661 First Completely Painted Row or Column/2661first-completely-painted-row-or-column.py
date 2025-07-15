class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:

        rows = defaultdict(int)
        cols = defaultdict(int)
        hmap = {}

        for y in range(len(mat)):
            for x in range(len(mat[0])):
                hmap[mat[y][x]] = (y, x)

        for i in range(len(arr)):
            y, x = hmap[arr[i]]
            rows[y] += 1
            cols[x] += 1
            if rows[y] == len(mat[0]) or cols[x] == len(mat):
                return i
        
        