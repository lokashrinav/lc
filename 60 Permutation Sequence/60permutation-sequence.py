class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k -= 1
        res = []
        arr = [str(i) for i in range(1, n + 1)]
        for i in range(n, 0, -1):
            x = math.factorial(i - 1)
            fun = k // x
            rem = k % x
            res.append(arr.pop(fun))
            k = rem
        
        return ''.join(res)

        