class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        '''
        [
            17, 5
            2, 5
            17, 16
        ]
        '''

        dp = [[0] * 3 for i in range(len(costs))]

        for i in range(len(costs)):
            if i == 0:
                dp[i] = costs[i]
            else:
                dp[i][0] = costs[i][0] + min(dp[i - 1][1], dp[i - 1][2])
                dp[i][1] = costs[i][1] + min(dp[i - 1][0], dp[i - 1][2])
                dp[i][2] = costs[i][2] + min(dp[i - 1][0], dp[i - 1][1])
        
        return min(dp[-1])