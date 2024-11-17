class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [defaultdict(int) for i in range(len(nums) + 1)]
        dp[0][0] = 1
        
        for i in range(len(nums)):
            for total, item in dp[i].items():
                dp[i + 1][total + nums[i]] += item
                dp[i + 1][total - nums[i]] += item
        print(dp)
        return dp[len(nums)][target]
