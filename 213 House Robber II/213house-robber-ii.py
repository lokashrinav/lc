class Solution:      
    def rob(self, nums: List[int]) -> int:
        def rob2(nums: List[int]) -> int:
            '''
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
            '''

            dp = [0] * (len(nums) + 2)
            for i in range(len(nums) - 1, -1, -1):
                dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
            
            return dp[0]
        
        if len(nums) == 1:
            return nums[0]

        return max(rob2(nums[:-1]), rob2(nums[1:]))

