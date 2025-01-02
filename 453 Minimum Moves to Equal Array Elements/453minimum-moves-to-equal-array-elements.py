class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minNum = min(nums)
        total = 0
        for i in range(len(nums)):
            total += (nums[i] - minNum)
        
        return total

        
        