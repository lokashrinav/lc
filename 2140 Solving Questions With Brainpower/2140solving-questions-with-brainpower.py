class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        memo = {}
        def dfs(ind):
            if ind >= len(questions):
                return 0
            if ind in memo:
                return memo[ind]

            memo[ind] = max(dfs(ind + 1), questions[ind][0] + dfs(ind + 1 + questions[ind][1]))

            return memo[ind]
        
        return dfs(0)
        