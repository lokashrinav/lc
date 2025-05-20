class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:

        res = [0] * (len(nums) + 1)

        for i in range(len(queries)):
            res[queries[i][0]] += 1
            res[queries[i][1] + 1] -= 1
        
        for i in range(1, len(res)):
            res[i] += res[i - 1]
        
        for i in range(len(nums)):
            if nums[i] > res[i]:
                return False
        
        return True
        
        