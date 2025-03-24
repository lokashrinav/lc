class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        l, r = 0, 1
        maxNum = 0
        total = 0

        if len(nums) < 3:
            return 0

        while l < len(nums) and r < len(nums):
            prev = None
            maxNum = 0
            while r < len(nums) and ((prev is not None and nums[r] - nums[r - 1] == prev) or prev is None):
                maxNum = max(maxNum, r - l + 1)
                prev = nums[r] - nums[r - 1]
                r += 1
            
            if maxNum >= 3:
                num = maxNum
                count = 1
                while num >= 3:
                    total += count
                    count += 1
                    num -= 1
            
            l = r - 1
        
        return total

        

