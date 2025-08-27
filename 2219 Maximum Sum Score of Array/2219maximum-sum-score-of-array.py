class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        prefix = [0]

        for i in range(len(nums)):
            prefix.append(prefix[-1] + nums[i])
        
        maxSum = float('-inf')
        sum1 = sum(nums)

        for i in range(len(nums)):
            maxSum = max(max(prefix[i + 1], sum1 - prefix[i]), maxSum)
            # print(prefix[i + 1], sum1 - prefix[i])
        
        return maxSum
        

            
        

        