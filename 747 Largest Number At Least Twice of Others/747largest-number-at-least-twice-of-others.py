class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxNum = max(nums)

        ind = nums.index(maxNum)

        for i in range(len(nums)):
            if i == ind:
                continue
            if maxNum >= 2 * nums[i]:
                continue
            else:
                return -1
        
        return ind
        