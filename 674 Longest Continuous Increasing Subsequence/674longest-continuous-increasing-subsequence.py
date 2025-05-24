class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        
        prev = nums[0]
        maxNum = 1
        curr = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i - 1]:
                curr += 1
            else:
                curr = 1
            maxNum = max(maxNum, curr)
        
        return maxNum
                
                
            
            
            
                
        