class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:


        '''

        1, 2, 3, 5, 6

        '''
        
        nums.sort()

        curr = None
        minNum = nums[0]
        maxNum = nums[0]
        final = 0
        for i in range(len(nums)):
            maxNum = max(nums[i], maxNum)
            minNum = min(minNum, nums[i])
            if maxNum - minNum > k:
                final += 1
                minNum = nums[i]
                maxNum = nums[i]
        
        return final + 1
        
        

