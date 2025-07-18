class Solution:
    def mySqrt(self, x: int) -> int:

        l, r = 0, x
        saved = 0

        while l <= r:
            m = (l + r) // 2
            if m * m <= x:
                saved = max(m, saved)
                l = m + 1
            else:
                r = m - 1

        return saved
        