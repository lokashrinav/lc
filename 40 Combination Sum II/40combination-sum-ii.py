class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        final = []
        candidates.sort()
        def helper(arr, sum1, index):
            if sum1 == target:
                final.append(arr.copy())
                return
            if sum1 > target or index >= len(candidates):
                return
            arr.append(candidates[index])
            helper(arr, sum1 + candidates[index], index + 1)
            arr.pop()
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            helper(arr, sum1, index + 1)

        '''

        1, 2, 2, 2, 5

        [1], []]

        '''
        
        helper([], 0, 0)
        return final
        

        