class Solution:
    def myPow(self, x: float, n: int) -> float:
        # (2, 10)
        # (2, 5)
        def dfs(x, n):
            if x == 1 or n == 0:
                return 1

            curr = dfs(x, n // 2)
            
            return curr * curr * x if n % 2 else curr * curr

        fun = dfs(x, abs(n))

        return fun if n >= 0 else (1 / fun)



        