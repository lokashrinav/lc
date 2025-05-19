class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        
        maxNum = max(nums[:(len(nums)-k+1)])

        ind = nums.index(maxNum)
        res = []

        for i in range(ind, ind + k):
            res.append(nums[i])
        
        return res



            




