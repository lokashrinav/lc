class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        '''
        [5, 1, 6]
        '''

        curr = 0
        for i in range(len(nums)):
            curr |= nums[i]
        
        return curr * (1 << (len(nums) - 1))


        '''

        [5, 4, 2]
        [2, 3, 6]

        '''
        
        return total
