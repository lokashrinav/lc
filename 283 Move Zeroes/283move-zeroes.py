class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        for i in range(len(nums)):
            while p1 < len(nums) and nums[p1] == 0:
                p1 += 1
            if p1 >= len(nums):
                nums[i] = 0
            else:
                nums[i] = nums[p1]
            p1 += 1
        
        
        

            

    
        