class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        final = []
        def helper(arr, sum1, index):
            if sum1 > target or index >= len(candidates):
                return
            if sum1 == target:
                final.append(arr.copy())
                return
            arr.append(candidates[index])
            helper(arr, sum1 + candidates[index], index)
            arr.pop()
            helper(arr, sum1, index + 1)
        
        helper([], 0, 0)
        return final
        