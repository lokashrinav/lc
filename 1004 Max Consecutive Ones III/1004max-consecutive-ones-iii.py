class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeroCount = 0
        count = 0
        maxCount = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                maxCount = max(count, maxCount)
            else:
                zeroCount += 1
                while zeroCount > k:
                    if nums[left] == 0:
                        zeroCount -= 1
                    left += 1
                count = i - left + 1
                maxCount = max(count, maxCount)
        return maxCount
                