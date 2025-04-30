class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        '''
        001
        100
        '''
        count = 0

        while x or y:
            a = x & 1
            b = y & 1
            if a != b:
                count += 1
            x = x >> 1
            y = y >> 1

        return count
