class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        l, r = 1, max(ribbons)
        maxNum = float('-inf')
        while l <= r:
            m = (l + r) // 2
            total = 0
            print(l, r, m)
            for i in range(len(ribbons)):
                total += (ribbons[i] // m)

            if total >= k:
                maxNum = m
                l = m + 1
            else:
                r = m - 1

        return maxNum if maxNum != float('-inf') else 0
