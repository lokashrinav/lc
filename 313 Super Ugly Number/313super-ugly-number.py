class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = []
        multiple = primes[:]
        indices = [0] * len(primes)
        dp.append(1)

        for i in range(n - 1):
            minNum = min(multiple)
            dp.append(minNum)

            for p in range(len(primes)):
                if multiple[p] == minNum:
                    indices[p] += 1
                    multiple[p] = primes[p] * dp[indices[p]]

        return dp[-1]

        


        