import math
class Solution:
    def numSquares(self, n: int) -> int:

        '''
        [0, 1, 2, 3, 1, 2, 3, 4, 2, 1, ]
        '''

        dp = [0] * (n + 1)

        coins = [1]

        for i in range(1, n + 1):
            x = math.sqrt(i)
            if(x % 1 == 0):
                coins.append(i)
            minNum = float('inf')
            for p in coins:
                minNum = min(1 + dp[i - p], minNum)
            dp[i] = minNum
        return dp[-1]




        