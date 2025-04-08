class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        '''
            4 + 2 + 6
            4 + 3 + 6
            4 + 3 + 2
            
        '''

        sum1 = sum(nums)

        i = 0
        total = 0
        for i in range(len(nums)):
            total += i * nums[i]
        
        maxNum = total

        for i in range(len(nums) - 1, -1, -1):
            total += sum1 - (len(nums) * nums[i])
            maxNum = max(maxNum, total)
        
        '''
            0 * 4 + 1 * 3 + 2 * 2 + 3 * 6
            1 * 4 + 2 * 3 + 3 * 2 + 4 * 6
        '''
        
        
        return maxNum







        