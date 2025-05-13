class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:

        total = 0
        memo = {}

        def dfs(char, num):
            if num == 0:
                return 1

            diff = 26 - (ord(char) - 97)

            if (num - diff) in memo:
                return memo[(num - diff)]
        
            # print(char, diff, t)

            if diff <= num:
                memo[(num - diff)] = (dfs('a', num - diff) + dfs('b', num - diff)) % (10 ** 9 + 7)
            else:
                memo[(num - diff)] = dfs(chr(ord(char) + 1), num - 1) % (10 ** 9 + 7)
            
            return memo[(num - diff)]
                
        total = 0
        for i in range(len(s)):
            total += dfs(s[i], t) % (10 ** 9 + 7)
        
        return total % (10 ** 9 + 7)