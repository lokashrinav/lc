class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        count = 0
        # -2, 0, 1, 3
        # i = 0, l = 1, r = 3
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1 
            changed = 0
            while l < r:
                if nums[i] + nums[l] + nums[r] >= target:
                    r -= 1
                else:
                    count += (r - l)
                    l += 1
        
        return count
