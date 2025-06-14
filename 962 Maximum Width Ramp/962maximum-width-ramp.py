class Solution:

    def maxWidthRamp(self, nums: List[int]) -> int:


        '''

        5, 8, 

        '''

        stack = []
        stack2 = []
        maxWidth = 0

        for i in range(len(nums) - 1, -1, -1):
            if not stack:
                stack.append(nums[i])
                stack2.append(i)
            else:
                ind = bisect_left(stack, nums[i])
                if ind < len(stack2):
                    maxWidth = max(maxWidth, stack2[ind] - i)
                    
                if nums[i] > stack[-1]:
                    stack.append(nums[i])   
                    stack2.append(i)               
        
        return maxWidth

        

        
        