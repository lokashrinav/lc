class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            m = (l + r) // 2
            print(m)
            if m * m == x:
                return m
            if m * m > x and (m - 1) * (m - 1) < x:
                return m - 1
            if m * m > x:
                r = m - 1
            elif m * m < x:
                l = m + 1

        return m
        

        