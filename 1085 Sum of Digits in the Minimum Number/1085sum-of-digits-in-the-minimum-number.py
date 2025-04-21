class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:

        minNum = min(nums)

        total = 0
        for elem in str(minNum):
            total += int(elem)
        
        return (total % 2 ^ 1)
        