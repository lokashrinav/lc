class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        res = []
        for i in range(len(nums)):
            for p in range(len(nums[i])):
                res.append((i + p, -i, nums[i][p]))
        
        res.sort(key=lambda x: (x[0], x[1], x[2]))

        return [val for i, x, val in res]

        