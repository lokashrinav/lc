class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        average = statistics.median(nums)
        num1, num2 = int(average), int(average) + 1
        sum1, sum2 = 0, 0
        for i in range(len(nums)):
            sum1 += abs(num1 - nums[i])
            sum2 += abs(num2 - nums[i])
        
        return min(sum1, sum2)
        