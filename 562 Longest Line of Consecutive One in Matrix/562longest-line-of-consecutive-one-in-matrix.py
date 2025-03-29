class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        
        longest = 0

        for i in range(len(mat)):
            longestCommon = 0
            for p in range(len(mat[0])):
                if mat[i][p] == 1:
                    longestCommon += 1
                else:
                    longestCommon = 0
                longest = max(longest, longestCommon)

        for p in range(len(mat[0])):
            longestCommon = 0
            for i in range(len(mat)):
                if mat[i][p] == 1:
                    longestCommon += 1
                else:
                    longestCommon = 0
                longest = max(longest, longestCommon)
        
        for i in range(len(mat[0])):
            w, h = i, 0
            longestCommon = 0
            while w < len(mat[0]) and h < len(mat):
                if mat[h][w] == 1:
                    longestCommon += 1
                else:
                    longestCommon = 0
                longest = max(longest, longestCommon)
                w += 1
                h += 1

        for i in range(len(mat)):
            w, h = 0, i
            longestCommon = 0
            while w < len(mat[0]) and h < len(mat):
                if mat[h][w] == 1:
                    longestCommon += 1
                else:
                    longestCommon = 0
                longest = max(longest, longestCommon)
                w += 1
                h += 1

        for i in range(len(mat[0])):
            w, h = i, len(mat) - 1
            longestCommon = 0
            while w < len(mat[0]) and h >= 0:
                if mat[h][w] == 1:
                    longestCommon += 1
                else:
                    longestCommon = 0
                longest = max(longest, longestCommon)
                w += 1
                h -= 1

        for i in range(len(mat)):
            w, h = 0, i
            longestCommon = 0
            while w < len(mat[0]) and h >= 0:
                if mat[h][w] == 1:
                    longestCommon += 1
                else:
                    longestCommon = 0
                longest = max(longest, longestCommon)
                w += 1
                h -= 1
        
        return longest
