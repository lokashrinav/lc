class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        

        suffix = [0]
        for i in range(len(nums) - 1, -1, -1):
            suffix.append(max(suffix[-1], nums[i]))
        
        suffix.reverse()

        prefix = nums[0]
        maxNum = 0
        for i in range(1, len(nums)):
            maxNum = max(maxNum, (prefix - nums[i]) * suffix[i + 1])
            prefix = max(prefix, nums[i])
        
        return maxNum
