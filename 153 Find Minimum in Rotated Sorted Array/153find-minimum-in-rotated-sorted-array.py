class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        currMin = float('inf')      

        # [3,4,5,1,2]
        while l <= r:
            m = (l + r) // 2
            if nums[l] <= nums[m]:
                currMin = min(nums[l], currMin)
                l = m + 1
            elif nums[m] <= nums[r]:
                currMin = min(nums[m], currMin)
                r = m - 1
        
        return currMin

