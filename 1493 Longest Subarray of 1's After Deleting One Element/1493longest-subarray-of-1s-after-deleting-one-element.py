class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        count = 0
        prev = False
        start = 0
        maxCount = 0
        for i in range(len(nums)):
            if prev and nums[i] == 0:
                while nums[start] != 0:
                    start += 1
                    count -= 1
                start += 1
            elif nums[i] == 0:
                prev = True
                count += 1
            else:
                count += 1

            if prev:
                maxCount = max(count - 1, maxCount)
            else:
                maxCount = max(count, maxCount)
        
        return maxCount if sum(nums) != len(nums) else len(nums) - 1

