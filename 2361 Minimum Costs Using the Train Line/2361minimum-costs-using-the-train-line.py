class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        
        '''
        dp[i][0] = max(dp[i + 1][1] + expressCost + express[i], dp[i + 1][0] + regular[i]) 
        dp[i][1] = max(dp[i + 1][0] + regular[i], dp[i + 1][1] + express[i]) 

        dp[i][0] = min(dp[i - 1][1] + regular[i], dp[i - 1][0] + regular[i]) 
        dp[i][1] = min(dp[i - 1][0] + express[i] + expressCost, dp[i - 1][1] + express[i]) 

        '''

        dp = [[0, 0] for i in range(len(express) + 1)]
        dp[0][0] = 0           # you're on regular to start
        dp[0][1] = expressCost # if you want to switch immediately

        for i in range(1, len(regular) + 1):
            dp[i][0] = min(dp[i - 1][1] + regular[i - 1], dp[i - 1][0] + regular[i - 1]) 
            dp[i][1] = min(dp[i - 1][0] + express[i - 1] + expressCost, dp[i - 1][1] + express[i - 1]) 
        
        print(dp)

        res = []
        for y in range(1, len(dp)):
            res.append(min(dp[y][0], dp[y][1]))
        
        return res
