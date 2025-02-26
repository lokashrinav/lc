class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
                
            if i == len(s) and j == len(p):
                return True
            
            if i > len(s) or j >= len(p):
                return False
            
            if p[j] == "*":
                cache[(i, j)] = dfs(i + 1, j) or dfs(i, j + 1)
                return cache[(i, j)]
            
            if i < len(s) and s[i] == p[j] or p[j] == "?":
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            
            cache[(i, j)] = False

            return cache[(i, j)]
        
        cache = {}       

        return dfs(0, 0)