class Solution:
    def numberOfCuts(self, n: int) -> int:

        '''
        even = n // 2
        odd = n


        '''

        if n == 1:
            return 0

        return n // 2 if n % 2 == 0 else n
        