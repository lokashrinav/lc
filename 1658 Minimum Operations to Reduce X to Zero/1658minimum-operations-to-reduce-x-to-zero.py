class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        '''

        4, 2


        1, 2, 6, 8, 11
        11, 10, 9, 5, 3
        '''

        hmap = {0:0}
        sum1 = 0
        for i in range(len(nums)):
            sum1 += nums[i]
            hmap[sum1] = i + 1

        minDiff = float('inf')
        if x in hmap:
            minDiff = min(minDiff, hmap[x])
                
        sum1 = 0
        for i in range(len(nums) - 1, -1, -1):
            sum1 += nums[i]
            if sum1 > x:
                break
            if x - sum1 in hmap and hmap[x - sum1] - 1 < i:
                minDiff = min(hmap[x - sum1] + len(nums) - i, minDiff)
        
        print(hmap, minDiff)
            
        return minDiff if float('inf') != minDiff else -1


        