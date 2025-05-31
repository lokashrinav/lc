class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        '''

        0, 1, 1, 2
        
        4, 5

        2, 3

        

        '''

        if n == 0:
            return 0

        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            if i % 2 == 0:
                dp[i] = dp[i // 2] 
            else:
                dp[i] = dp[(i - 1) // 2] + dp[((i - 1) // 2) + 1]
        
        print(dp)

        return max(dp)



        