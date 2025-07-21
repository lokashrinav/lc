class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[-1] = True  # We can always reach the end from the end

        for i in range(n - 2, -1, -1):
            farthest = min(i + nums[i], n - 1)
            for j in range(i + 1, farthest + 1):
                if dp[j]:
                    dp[i] = True

        return dp[0]


                    

        

            