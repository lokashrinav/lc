class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        ops = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                nums[i] = 1
                nums[i + 1] = 1 if nums[i + 1] == 0 else 0
                nums[i + 2] = 1 if nums[i + 2] == 0 else 0
                ops += 1
                
        print(nums)
        
        return ops if sum(nums) == len(nums) else -1