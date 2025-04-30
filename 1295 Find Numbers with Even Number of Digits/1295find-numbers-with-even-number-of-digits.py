class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        total = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                total += 1
        
        return total