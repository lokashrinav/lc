class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        
        # y = 3, x = 5, target = 4

        '''
        39 - 24 = 15

        cx = y - target / x)

        x = 34 -> 29 -> 24 -> 19 -> 14 -> 9 -> 4
        x = 33 -> 28 -> 23 -> 18 -> 13 -> 8 -> 3
        x = 32 -> 27 -> 22 -> 17 -> 12 -> 7 -> 2
        x = 31 -> 26 -> 21 -> 16 -> 11 -> 6 -> 1

        (y - target) / x

        c < 2 = 5'''

        if target > x + y:
            return False
        
        return gcd(x, y) == gcd(x, y, target)