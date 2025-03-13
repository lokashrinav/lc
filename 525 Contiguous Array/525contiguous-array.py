class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        prefix = 0
        hmap = {0:-1}
        maxNum = 0
        for i in range(len(nums)):
            prefix += 1 if nums[i] else -1
            if prefix in hmap:
                maxNum = max(i - hmap[prefix], maxNum)
            else:
                hmap[prefix] = i
        
        return maxNum

        '''

        -1 0 1 2 3 4 3 2 1

        '''

        
            
        