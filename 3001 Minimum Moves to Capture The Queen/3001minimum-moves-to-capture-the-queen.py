class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        
        '''

        '''

        minNum = 2
        if a == e and e == c:
            if b >= d >= f or b <= d <= f:
                return 2

        if b == d and d == f:
            if a >= c >= e or a <= c <= e:
                return 2

        if a == e or b == f:
            minNum = 1

        if minNum == 1:
            return 1

        if (d - c) == (f - e) and (f - e) == (b - a):
            if c >= a >= e or c <= a <= e:
                return 2
    
        if (d + c) == (f + e) and (d + c) == (a + b):
            if c >= a >= e or c <= a <= e:
                return 2

        if (d - c) == (f - e) or (d + c) == (f + e):
            minNum = 1

        return minNum
