class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:

        def helper(nums, idk):
            print(nums, idk)
            for i in range(1, len(nums)):
                if nums[i] < nums[i - 1]:
                    if idk:
                        return False
                    saved = nums[i - 1]
                    nums[i - 1] = nums[i]
                    if helper(nums, True):
                        return True
                    nums[i - 1] = saved

                    nums[i] = nums[i - 1]
                    if helper(nums, True):
                        return True
                    
                    return False
            return True
            
        return helper(nums, False)

                
