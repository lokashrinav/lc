class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        count = 0
        l = 0
        longest = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1

            while count > k:
                if nums[l] == 0:
                    count -= 1
                l += 1
            
            longest = max(longest, i - l + 1)
        
        return longest
        