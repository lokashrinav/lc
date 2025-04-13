class Solution:
    def countGoodNumbers(self, n: int) -> int:
        prime = ['2', '3', '5', '7']
        evens = ['0', '2', '4', '6', '8']

        # if n > ((10 ** + 7) / 20):

        idk = pow(5, (n + 1) // 2, 10 ** 9 + 7)
        idk *= pow(4, n // 2, 10 ** 9 + 7)

        return idk % (10 ** 9 + 7)

        '''
        5 ** ((n + 1) // 2)
        2 ** n

        1000
        100 * 100

        10000 * 1000

        100

        101 * 101 = 
        11001
        11001
        ---

        


        20 ** (n // 2) > (10 ** 9 + 7)

        n = 8

        return idk'''

        '''n = n % 20

        idk = len(evens) ** (n // 2)
        # idk = idk % (10 ** 9 + 7) 
        idk *= len(prime) ** (n // 2)
        # idk = idk % (10 ** 9 + 7) 
        if n % 2 == 1:
            idk *= len(evens)
            # idk = idk % (10 ** 9 + 7) 

        return idk'''

        '''
        10 -> 20 ** 5
        (20 ** (n // 2)) < (10 ** 9 + 7)
        20 < sqrt of (n // 2) ((10 ** 9) + 7)

        20 ** (n // 2)
        20 ** 24 > (10 ** 9 + 7)

        '''



                

        # (20 ** n // 2) < (10 ** 9 + 7)

        '''count = 1
        for i in range(n):
            if i % 2 == 0:
                count *= len(evens)
            else:
                count *= len(prime)
            count = count % (10 ** 9 + 7)
        return count'''
        