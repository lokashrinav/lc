class Solution:
    def rotatedDigits(self, n: int) -> int:

        '''
        6, 9, 2, 5

        23
        '''

        total = 0
        for i in range(1, n + 1):
            if '3' in str(i) or '4' in str(i) or '7' in str(i):
                continue
            if '6' in str(i) or '9' in str(i) or '2' in str(i) or '5' in str(i):
                total += 1
        
        return total
        