class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        total = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                total += nums[i]
        
        res = []

        for y, x in queries:
            if nums[x] % 2 == 0:
                total -= nums[x]
            nums[x] += y
            if nums[x] % 2 == 0:
                total += nums[x]

            res.append(total)
        
        return res
        