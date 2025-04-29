class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        maxNum = max(nums)
        count = 0

        l = 0
        total = 0
        r = len(nums)
        for i in range(len(nums)):
            if nums[i] == maxNum:
                count += 1
                        
            while count >= k:
                total += (r - i)
                if nums[l] == maxNum:
                    count -= 1
                l += 1
        
        return total


