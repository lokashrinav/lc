class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        memo = {}
        def dfs(ind, count_m, count_n):
            if ind >= len(strs):
                return 0
            
            if (ind, count_m, count_n) in memo:
                return memo[(ind, count_m, count_n)]
            
            calc = 0
            if count_m + strs[ind].count("0") <= m and count_n + strs[ind].count("1") <= n:
                calc = 1 + dfs(ind + 1, count_m + strs[ind].count("0"), count_n + strs[ind].count("1"))

            memo[(ind, count_m, count_n)] = max(dfs(ind + 1, count_m, count_n), calc)

            return memo[(ind, count_m, count_n)]
        
        calc = dfs(0, 0, 0)

        return calc
