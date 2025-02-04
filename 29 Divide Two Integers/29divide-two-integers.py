class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        # 1010
        # 101
        a, b = abs(dividend), abs(divisor)
        signed = (dividend > 0) ^ (divisor > 0)
        res = 0
        while a - b >= 0:
            x = 0
            while a - (b << 1 << x) >= 0:
                x += 1
            res += (1 << x)
            a -= (b << x)
        
        return res if not signed else -res

        