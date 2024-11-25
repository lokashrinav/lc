class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1]

        prime = [2, 3, 5]
        multiple = [2, 3, 5]
        indices = [0, 0, 0]

        for j in range(n - 1):
            minNum = min(multiple)
            dp.append(minNum)

            for i in range(len(multiple)):
                if multiple[i] == minNum:
                    indices[i] += 1
                    multiple[i] = prime[i] * dp[indices[i]]

        return dp[-1]




        