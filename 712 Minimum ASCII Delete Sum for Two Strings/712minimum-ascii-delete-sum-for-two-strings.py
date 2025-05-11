class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        memo = {}

        def dfs(i, j):
            if i == 0 or j == 0:
                return ("", 0)
            if (i, j) in memo:
                return memo[(i, j)]
            
            if s1[i - 1] == s2[j - 1]:
                str1, length = dfs(i - 1, j - 1)
                memo[(i, j)] = (str1 + s1[i - 1], ord(s1[i - 1]) + length)
            else:
                str1, length1 = dfs(i, j - 1)
                str2, length2 = dfs(i - 1, j)
                if length1 > length2:
                    memo[(i, j)] = (str1, length1)
                else:
                    memo[(i, j)] = (str2, length2)

            return memo[(i, j)]

        str1, length1 = dfs(len(s1), len(s2))

        hmap = Counter(str1)
        total = 0

        for i in range(len(s1)):
            if s1[i] not in hmap or hmap[s1[i]] == 0:
                total += ord(s1[i])
            else:
                hmap[s1[i]] -= 1
        
        hmap = Counter(str1)
        for i in range(len(s2)):
            if s2[i] not in hmap or hmap[s2[i]] == 0:
                total += ord(s2[i])
            else:
                hmap[s2[i]] -= 1
        
        return total
        



        