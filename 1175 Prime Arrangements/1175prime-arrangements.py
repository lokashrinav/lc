class Solution:
    def numPrimeArrangements(self, n: int) -> int:

        is_prime = [1] * (n + 1)
        is_prime[0] = 0
        is_prime[1] = 0
        p = 2

        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = 0

            p += 1

        count = 0
        for i in range(2, len(is_prime)):
            if is_prime[i]:
                count = ((count + 1) % (10 ** 9 + 7))

        print(n - count, count)

        '''

        2, 3, 5, 7 -> 

        6! * 5!

        '''
        
        return math.factorial(n - count) * math.factorial(count) % (10 ** 9 + 7)       


        