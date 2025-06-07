class Solution:
    def maximumAlternatingSubarraySum(self, nums: List[int]) -> int:
        
        maxNum = max(nums)
        curr = 0

        for i in range(0, len(nums), 2):
            curr += nums[i]
            maxNum = max(maxNum, curr)

            if i + 1 < len(nums):
                curr -= nums[i + 1]

            maxNum = max(maxNum, curr)

            if curr < 0:
                curr = 0
        
        curr = 0
        for i in range(1, len(nums), 2):
            curr += nums[i]
            maxNum = max(maxNum, curr)

            if i + 1 < len(nums):
                curr -= nums[i + 1]

            maxNum = max(maxNum, curr)

            if curr < 0:
                curr = 0
        
        return maxNum

        

        

        