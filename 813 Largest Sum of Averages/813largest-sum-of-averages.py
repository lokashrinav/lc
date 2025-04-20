class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        
        prefix = [0]

        for i in range(len(nums)):
            prefix.append(prefix[i] + nums[i])

        memo = {}

        def avg(i, j):
            return (prefix[j] - prefix[i]) / (j - i)

        def dp(i, left):
            if (i, left) in memo:
                return memo[(i, left)]

            j = len(nums)

            if left == 1:
                return avg(i, j)

            best = 0
            for p in range(i + 1, j - left + 2):
                best = max(best, avg(i, p) + dp(p, left - 1))

            memo[(i, left)] = best
            return best

        return dp(0, k)

        