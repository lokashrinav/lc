class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:

        nums.sort()

        '''

        -1, 1, 1, 2, 3


        '''

        l, r = 0, len(nums) - 1
        total = 0

        while l < r:
            if nums[l] + nums[r] < target:
                total += r - l
                l += 1
            else:
                r -= 1
        
        return total

        