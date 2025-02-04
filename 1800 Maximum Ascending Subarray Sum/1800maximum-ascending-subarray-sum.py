class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        count = None
        maxNum = 0
        for i in range(len(nums)):
            if not count:
                count = nums[i]
            else:
                if nums[i] > nums[i - 1]:
                    count += nums[i]
                else:
                    count = nums[i]

            maxNum = max(maxNum, count)
        
        return maxNum
                
            

        