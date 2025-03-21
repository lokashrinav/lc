class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:

        memo = defaultdict(str)
        used = set()

        def dfs(i, j):
            if i == len(pattern) and j == len(s):
                return True
            elif i >= len(pattern) or j >= len(s):
                return False

            if pattern[i] in memo:
                length = len(memo[pattern[i]])
                if memo[pattern[i]] != s[j:j+length]:
                    return False
                return dfs(i + 1, j + length)

            for p in range(j + 1, len(s) + 1):
                word = s[j:p]
                if word in used:
                    continue
                
                memo[pattern[i]] = word
                used.add(word)

                if dfs(i + 1, p):
                    return True
                
                del memo[pattern[i]]
                used.remove(word)
            
            return False
        
        return dfs(0, 0)

        