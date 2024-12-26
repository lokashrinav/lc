class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0
        arr = [True] * n
        arr[0], arr[1] = False, False

        
        for i in range(2, int(n ** 0.5) + 1):
            if arr[i]:
                for p in range(i * i, n, i):
                    arr[p] = False
        return sum(arr)

