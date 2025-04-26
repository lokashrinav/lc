class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:

        '''

        
        '''

        dp = [[0] * len(costs[0]) for i in range(len(costs))]

        dp[0] = costs[-1]

        for i in range(len(costs) - 2, -1, -1):
            minNum, minInd = float('inf'), 0
            minNum2, minInd2 = float('inf'), 0
            for p in range(len(costs[0])):
                if costs[i + 1][p] < minNum:
                    minNum = costs[i + 1][p]
                    minInd = p

            for p in range(len(costs[0])):
                if p == minInd:
                    continue
                if costs[i + 1][p] < minNum2:
                    minNum2 = costs[i + 1][p]
                    minInd2 = p

            for p in range(len(costs[0])):
                if p == minInd:
                    costs[i][p] += minNum2
                    continue

                costs[i][p] += minNum
        
        return min(costs[0])