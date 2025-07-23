class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''

        []

        '''

        dp = [1] * len(nums)

        for i in range(len(nums)):
            maxNum = 1
            for p in range(i - 1, -1, -1):
                if nums[i] > nums[p]:
                    maxNum = max(1 + dp[p], maxNum)
            dp[i] = maxNum
        
        print(dp)

        return max(dp)