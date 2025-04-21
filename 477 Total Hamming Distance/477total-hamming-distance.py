class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        
        bitLength = max(bit.bit_length() for bit in nums)
        total = 0
        for i in range(bitLength):
            one = 0
            for i in range(len(nums)):
                if nums[i] & 1 == 1:
                    one += 1
            zero = len(nums) - one
            total += one * zero

            for i in range(len(nums)):
                nums[i] = nums[i] >> 1
        
        return total

            
