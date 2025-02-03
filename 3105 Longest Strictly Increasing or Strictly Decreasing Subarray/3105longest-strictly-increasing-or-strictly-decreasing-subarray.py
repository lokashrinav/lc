class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        incLength = 1
        decLength = 1
        maxNum = float('-inf')

        if len(nums) == 1:
            return 1

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                decLength += 1
                incLength = 1
            elif nums[i] < nums[i + 1]:
                incLength += 1
                decLength = 1
            else:
                incLength = 1
                decLength = 1
            maxNum = max([incLength, maxNum, decLength])
        
        return maxNum
