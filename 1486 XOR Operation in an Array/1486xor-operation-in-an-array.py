class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        '''
        start, start + 2, start + 4, start + 6

        1, 3, 5, 7

        1

        '''
        xor = start
        for i in range(1, n):
            xor ^= 2 * i + start
        
        return xor

