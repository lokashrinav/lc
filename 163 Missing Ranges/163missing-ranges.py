class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower, upper]]
        elif len(nums) == 1:
            ranges = []
            if nums[0] > lower:
                ranges.append([lower, nums[0] - 1])
            if nums[-1] < upper:  
                ranges.append([nums[-1] + 1, upper])
            return ranges

        ranges = []
        for i in range(len(nums) - 1):
            if i == 0 and nums[i] > lower:
                ranges.append([lower, nums[i] - 1])
            if nums[i] != nums[i + 1] - 1:
                ranges.append([nums[i] + 1, nums[i + 1] - 1])
            if i + 1 == len(nums) - 1 and nums[i + 1] < upper:  
                ranges.append([nums[i + 1] + 1, upper])
        
        return ranges
        

