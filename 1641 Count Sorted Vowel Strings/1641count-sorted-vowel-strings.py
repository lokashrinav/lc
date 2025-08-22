class Solution:
    def countVowelStrings(self, n: int) -> int:

        arr = ["a","e","i","o","u"]
        '''
        n = 3

        a a a
        a a e
        a a i
        a a o
        a a u
        a e e
        a e i
        a e o
        a e u
        a i i
        a i o
        a i u
        a o o
        a o u
        a u u
        '''

        def dfs(left, i):
            if left == 0:
                return 1
            
            total = 0
            for p in range(i, len(arr)):
                total += dfs(left - 1, p)

            return total

        calc = dfs(n, 0)

        return calc        