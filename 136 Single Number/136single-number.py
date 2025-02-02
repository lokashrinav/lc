class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bit = 0 

        for i in range(len(nums)):
            bit = bit ^ nums[i]
        
        return bit
        