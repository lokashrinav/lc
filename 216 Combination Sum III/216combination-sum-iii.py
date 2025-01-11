class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(start, curr):
            if len(curr) == k and sum(curr) == n:
                return [curr.copy()]
            elif len(curr) >= k:
                return [[]]
            
            lis = []
            for i in range(start, 10):
                curr.append(i)
                calc = dfs(i + 1, curr)
                for l in calc:
                    if l:
                        lis.append(l)
                curr.pop()
            
            return lis
        
        return dfs(1, [])        