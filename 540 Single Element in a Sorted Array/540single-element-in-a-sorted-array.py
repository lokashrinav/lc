class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        '''
            [1,1,2,3,3,4,4,8,8]
        '''

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            condition1 = m + 1 == len(nums) or nums[m] != nums[m + 1]
            condition2 = m - 1 < 0 or nums[m] != nums[m - 1]
            if condition1 and condition2:
                break
            elif m - 1 >= 0 and nums[m] == nums[m - 1]:
                if (len(nums) - m) % 2:
                    r = m - 1
                else:
                    l = m + 1
            elif m + 1 < len(nums) and nums[m] == nums[m + 1]:
                if (len(nums) - m) % 2 == 0:
                    r = m - 1
                else:
                    l = m + 1
        
        return nums[m]