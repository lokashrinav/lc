class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        
        '''
        fac(n) = fac()

        1 to n, count the number of 5's, 2's and 10's of the factors of n

        n * sqrt(n)

        '''
        count = 0
        while n:
            n //= 5
            count += n
        return count

            