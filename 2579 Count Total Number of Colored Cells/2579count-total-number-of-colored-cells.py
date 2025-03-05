class Solution:
    def coloredCells(self, n: int) -> int:
        '''
        1
        4
        8
        12

        1,5, 13, 25

        '''
        '''if n == 1:
            return 1

        dp = [1]

        for i in range(n - 1):
            if dp[-1] == 1:
                dp.append(4)
            else:
                dp.append(dp[-1] + 4)

        sum1 = 0
        for i in range(len(dp)):
            sum1 += dp[i]
        return sum1'''

        '''
        n=n-1
        E i * 4 
        i=1

        2 * (n * n - 1) + 1

        '''

        return 2 * (n * (n - 1)) + 1



        