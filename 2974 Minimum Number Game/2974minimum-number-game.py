class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:

        
        ''' 

        3, 3, 4, 5

        '''

        nums.sort()

        for i in range(0, len(nums), 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        
        return nums


        