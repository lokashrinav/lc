class Solution:
    def check(self, nums: List[int]) -> bool:

        changed = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if changed:
                    return False
                changed = True
        
        if nums[-1] > nums[0] and changed:
            return False
        
        return True

        