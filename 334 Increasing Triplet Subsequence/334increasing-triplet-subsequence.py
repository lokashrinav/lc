class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        first, second = float('inf'), float('inf')
        for i in range(len(nums)):
            print(first, second)
            if nums[i] < first:
                first = nums[i]
            elif nums[i] > first and nums[i] < second:
                second = nums[i]
            elif nums[i] > second:
                return True
        
        return False
