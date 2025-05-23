class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:

        '''

        one away or two away

        '''

        arr = [a, b, c]

        arr.sort()

        a, b, c = arr

        if abs(a - b) == 1 and abs(b - c) == 1:
            calc = 0
        elif abs(a - b) == 1 or abs(c - b) == 1 or abs(a - b) == 2 or abs(b - c) == 2:
            calc = 1
        else:
            calc = 2

        res = [calc, max(a, b, c) - min(a, b, c) - 2]

        return res
        