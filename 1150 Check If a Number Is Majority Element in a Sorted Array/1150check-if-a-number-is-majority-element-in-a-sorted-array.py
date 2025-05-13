class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        
        calc = bisect_right(nums, target) - bisect_left(nums, target)
        return calc > len(nums) / 2