class Solution:
    def findMin(self, nums: List[int]) -> int:

        '''
            5, 5, 1, 2, 2, 3, 4

            2, 2, 2, 2, 2

            2, 2, 2, 3, 3
            
            2, 2, 3, 2, 2
        '''

        l, r = 0, len(nums) - 1
        currMin = float('inf')

        # 3, 0, 1, 1, 3

        while l <= r:
            m = (l + r) // 2
            if nums[m] == nums[r] and nums[m] == nums[l]:
                currMin = min(currMin, nums[m])
                r -= 1
                l += 1
            elif nums[m] == nums[r]:
                currMin = min(currMin, nums[r])
                r = m - 1
            elif nums[m] == nums[l]:
                currMin = min(currMin, nums[l])
                l = m + 1
            elif nums[m] > nums[r]:
                currMin = min(currMin, nums[r])
                l = m + 1
            elif nums[m] > nums[l]:
                currMin = min(currMin, nums[l])
                l = m + 1
            else:
                currMin = min(currMin, nums[m])
                r -= 1
                l += 1
        
        return currMin
        