class Solution:
    def countHillValley(self, nums: List[int]) -> int:

        res = []
        for i in range(len(nums)):
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            res.append(nums[i])
        
        nums = res

        print(nums)
        
        count = 0
        for i in range(1, len(nums) - 1):
            if nums[i + 1] < nums[i] > nums[i - 1]:
                count += 1
            elif nums[i + 1] > nums[i] < nums[i - 1]:
                count += 1
        
        return count
        