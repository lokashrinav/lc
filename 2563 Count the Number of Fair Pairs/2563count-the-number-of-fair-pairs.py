class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        nums.sort()

        '''
        0, 1, 4, 4, 5, 7
        '''

        total = 0
        for i in range(len(nums)):
            cl, cu = lower - nums[i], upper - nums[i]
            print(nums[i], cl, cu)
            if nums[i] >= cl:
                num = bisect_left(nums, cl, 0, i)
                num2 = bisect_right(nums, cu, 0, i)
                total += num2 - num
        
        return total
