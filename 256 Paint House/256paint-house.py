class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        '''
        
        dp[i][0] = max(dp[i - 1][1], dp[i - 1][2])

        '''

        dp = [[0] * 3 for _ in range(len(costs) + 1)]
        for i in range(1, len(costs) + 1):
            for p in range(3):
                dp[i][p] = min(dp[i - 1][(p + 1) % 3], dp[i - 1][(p + 2) % 3]) + costs[i - 1][p]
        
        return min(dp[-1])