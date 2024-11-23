class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # [1]
        # [1, 1]
        # [1, 2, 1]
        # [0, 0, 0, 0, 0]
        dp = [0, 1, 0]

        final = [[1]]

        for i in range(numRows - 1):
            dp2 = []
            for p in range(1, len(dp)):
                dp2.append(dp[p] + dp[p - 1])
            final.append(dp2.copy())
            dp2.append(0)
            dp2 = [0] + dp2
            dp = dp2
        return final
        