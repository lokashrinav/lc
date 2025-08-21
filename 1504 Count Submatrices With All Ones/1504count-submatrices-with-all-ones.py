class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        h = [0] * n          # height of consecutive 1s ending at current row
        ans = 0

        for i in range(m):
            # update heights
            for j in range(n):
                h[j] = h[j] + 1 if mat[i][j] == 1 else 0

            # count rects with bottom row = i
            for j in range(n):
                if h[j] == 0: 
                    continue
                minH = h[j]
                k = j
                while k >= 0 and h[k] > 0:
                    minH = min(minH, h[k])
                    ans += minH
                    k -= 1

        return ans
