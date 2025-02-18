class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        idk = [0] * len(nums)

        for i in range(len(nums)):
            idk[i] = nums[nums[i]]
        
        return idk
        