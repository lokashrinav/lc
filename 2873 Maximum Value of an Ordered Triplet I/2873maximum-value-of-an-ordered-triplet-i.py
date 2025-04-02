class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:


        maxNum = 0
        prefix = 0
        suffix = 0

        n = len(nums)

        suffix_max = [0] * n
        suffix_max[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], nums[i])
            
        for i in range(1, len(nums) - 1):
            prefix = max(prefix, nums[i - 1])
            maxNum = max((prefix - nums[i]) * suffix_max[i + 1], maxNum)
        
        return maxNum

