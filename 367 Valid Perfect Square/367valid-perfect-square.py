class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 0
        r = num
        while l <= r:
            m = (l + r) // 2
            if m * m > num:
                r = m - 1
            elif m * m == num:
                return True
            else:
                l = m + 1
        return False
        