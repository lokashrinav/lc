class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        dp = [[0 for i in range(len(nums))] for p in range(len(nums))]
        
        for i in range(len(nums)):
            for p in range(len(nums)):
                if i == p:
                    dp[i][p] = nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            for p in range(i + 1, len(nums)):
                dp[i][p] = max(nums[i] - dp[i + 1][p], nums[p] - dp[i][p - 1])
        
        return dp[0][len(nums) - 1] >= 0
                    