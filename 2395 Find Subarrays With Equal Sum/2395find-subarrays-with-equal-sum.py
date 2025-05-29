class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        
        sum1 = 0
        for i in range(2):
            sum1 += nums[i]

        hset = set([sum1])

        for i in range(len(nums) - 2):
            sum1 += nums[i + 2]
            sum1 -= nums[i]
            if sum1 in hset:
                return True
            hset.add(sum1)
        
        return False
            
            
        