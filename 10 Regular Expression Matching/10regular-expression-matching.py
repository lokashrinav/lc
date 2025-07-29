class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @lru_cache(maxsize=None)
        def dfs(i, j):
            print(i, j)
            if i == len(s):
                if j == len(p):
                    return True
                if j + 1 < len(p) and p[j + 1] == "*":
                    return dfs(i, j + 2)
                return False
            if j >= len(p):
                return False
            if j + 1 < len(p) and p[j:j + 2] == ".*":
                return dfs(i + 1, j) or dfs(i, j + 2)
            if s[i] != p[j] and j + 1 < len(p) and p[j + 1] == "*":
                return dfs(i, j + 2)
            if s[i] == p[j] and j + 1 < len(p) and p[j + 1] == "*":
                if i == 4 and j == 2:
                    print("HELLO")
                return dfs(i, j + 2) or dfs(i + 1, j)
            if s[i] == p[j] or p[j] == ".":
                return dfs(i + 1, j + 1)

            return False

        return dfs(0, 0)