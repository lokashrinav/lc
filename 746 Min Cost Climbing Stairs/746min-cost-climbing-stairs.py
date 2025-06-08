class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        hmap = {}

        def dfs(i):
            if i >= len(cost):
                return 0

            if i in hmap:
                return hmap[i]

            minCost = cost[i] + dfs(i + 1)

            minCost = min(minCost, cost[i] + dfs(i + 2))

            hmap[i] = minCost

            return minCost

        return min(dfs(0), dfs(1))
        