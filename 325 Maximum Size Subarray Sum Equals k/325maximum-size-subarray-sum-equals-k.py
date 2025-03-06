class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        '''
        1, 0, 5, 3, 6, 6
        '''

        hmap = {0:-1}
        maxNum = 0
        prev = 0
        # 1, 0, 5, 3
        for i in range(len(nums)):
            prev += nums[i]
            if prev - k in hmap:
                maxNum = max(i - hmap[prev - k], maxNum)
            if prev in hmap:
                continue
            else:
                hmap[prev] = i

        return maxNum

        # 


