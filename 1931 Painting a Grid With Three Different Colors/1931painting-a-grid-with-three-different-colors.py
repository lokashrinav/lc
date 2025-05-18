class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:

        valid = []
        def dfs(curr):
            if len(curr) == m:
                valid.append(curr.copy())
                return
            
            for i in range(3):
                if curr and i == curr[-1]:
                    continue
                curr.append(i)
                dfs(curr)
                curr.pop()
        
        dfs([])

        comp = defaultdict(list)

        for i in range(len(valid)):
            for p in range(len(valid)):
                flag = True
                for v in range(len(valid[i])):
                    if valid[i][v] == valid[p][v]:
                        flag = False
                
                if flag:
                    comp[i].append(p)

        MOD = (10 ** 9) + 7

        dp = [1] * len(valid)
        for i in range(n - 1):
            new_dp = [0] * len(valid)
            for p in range(len(valid)):
                for elem in comp[p]:
                    new_dp[elem] = (new_dp[elem] + dp[p]) % MOD
            dp = new_dp

        return sum(dp) % MOD




