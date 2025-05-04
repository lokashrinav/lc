class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        if 1 in nums:
            return n - nums.count(1)
        
        if reduce(gcd, nums) > 1:
            return -1
        
        return n