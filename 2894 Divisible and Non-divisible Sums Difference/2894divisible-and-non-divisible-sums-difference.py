class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:

        '''
        n // m = 10 // 3, m + 2 * m + 3 *m


        m * (1 + 2 + 3)
        '''

        count = n // m
        total = 0

        res = m * (count * (count + 1) // 2)

        res2 = (n * (n + 1) // 2) - res

        print(res, res2)

        return res2 - res



        