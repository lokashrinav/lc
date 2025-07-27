class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        curr = []
        sum1 = 0
        def dfs(ind, sum1):
            if sum1 > target:
                return 
            if sum1 == target:
                res.append(curr.copy())
            if ind == len(candidates):
                return 

            for i in range(ind, len(candidates)):
                curr.append(candidates[i])
                sum1 += candidates[i]
                dfs(i, sum1)
                sum1 -= candidates[i]
                curr.pop()
        
        dfs(0, 0)

        return res
        