class Solution:
    def maxSum(self, nums: List[int]) -> int:

        hmap = {}

        for i in range(len(nums)):
            maxNum = 0
            for elem in str(nums[i]):
                maxNum = max(int(elem), maxNum)
            
            if maxNum not in hmap:
                hmap[maxNum] = [-1, -1]
            
            if nums[i] > hmap[maxNum][0]:
                hmap[maxNum][1] = hmap[maxNum][0] 
                hmap[maxNum][0] = nums[i]
            elif nums[i] > hmap[maxNum][1]:
                hmap[maxNum][1] = nums[i]
        
        maxSum = -1

        for key in hmap:
            val1, val2 = hmap[key]

            if val2 == -1 or val1 == -1:
                continue
            
            maxSum = max(val1 + val2, maxSum)

        return maxSum

        