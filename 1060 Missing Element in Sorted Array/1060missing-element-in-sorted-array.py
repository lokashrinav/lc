class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:

        l, r = 0, len(nums) - 1
        m = 0

        while l < r:
            m = (l + r) // 2
            if nums[m] - nums[0] - m >= k:
                r = m
            else:
                l = m + 1
        
        print(l)
        
        if l == len(nums) - 1 and k > (nums[l] - nums[0] - l):
            calc = k - (nums[l] - nums[0] - l)
            return nums[l] + calc
        else:
            calc = (nums[l] - nums[0] - l)
            diff = abs(k - calc)
            return nums[l] - diff - 1
        


        