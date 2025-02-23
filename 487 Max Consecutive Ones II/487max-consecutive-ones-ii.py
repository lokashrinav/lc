class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        p2 = i = 0
        maxCount = count = 0

        while i < len(nums):
            p2 = i + 1
            prevCount = count + 1
            total = 0
            if nums[i] == 0:
                while p2 < len(nums) and nums[p2] == 1:
                    total += 1
                    p2 += 1
                maxCount = max(prevCount + total, maxCount)
                i = p2 - 1             
                count = total
            else:
                count += 1
                maxCount = max(count, maxCount)
            i += 1
        
        return maxCount
        

        