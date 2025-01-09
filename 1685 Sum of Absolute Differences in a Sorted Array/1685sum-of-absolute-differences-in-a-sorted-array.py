class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = []
        left, right = 0, sum(nums)
        for i in range(len(nums)):
            curr = right - nums[i]
            leftSum = nums[i] * i - left
            rightSum = curr - nums[i] * (n - i - 1)

            res.append(leftSum + rightSum)

            right -= nums[i]
            left += nums[i]
        
        return res




