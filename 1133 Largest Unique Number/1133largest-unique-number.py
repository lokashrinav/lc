class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        
        hmap = Counter(nums)
        minNum = -1
        for i in range(len(nums)):
            if hmap[nums[i]] == 1:
                minNum = max(minNum, nums[i])
        
        return minNum