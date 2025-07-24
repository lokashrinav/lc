class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        '''
            dp[0] = 1
            dp[1] = 1
            dp[2] = 
        '''

        dp = [1] * len(nums)
        dp2 = [1] * len(nums)

        for i in range(len(nums)):
            for p in range(i - 1, -1, -1):
                if nums[i] > nums[p]:
                    dp[i] = max(dp[i], 1 + dp[p])
            for p in range(i - 1, -1, -1):
                if nums[p] < nums[i] and dp[i] == dp[p] + 1:
                    dp2[i] += dp2[p]
            if dp2[i] != 1:
                dp2[i] -= 1
        
        print(dp, dp2)

        final = max(dp)

        answer = sum(c for l, c in zip(dp, dp2) if l == final)

        return answer


        
            


        
            