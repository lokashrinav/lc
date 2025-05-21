class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:

        nums.sort()

        stack = []
        total = 0

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                stack.append((i, nums[i]))
            
            k = abs(nums[i - 1] - nums[i]) - 1
            count = 1

            #print(stack, total)

            ''''

            1, 1, 2, 2, 3, 7

            1, 2
            '''

            while stack and k > 0:
                ind, num = stack.pop()
                total += (nums[i - 1] + count) - num
                count += 1
                k -= 1
                    
        '''
        1, 1, 2, 2, 3, 7
        stack: 1, 2
        '''
        
        count = 1
        while stack:
            ind, num = stack.pop()
            total += (nums[-1] + count) - num
            count += 1
        
        return total

        