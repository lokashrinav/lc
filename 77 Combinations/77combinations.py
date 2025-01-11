class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        lis = []
        def dfs(num, curr):
            if len(curr) >= k:
                lis.append(curr[:])
                return 
            elif num > n:
                return
            curr.append(num)
            dfs(num + 1, curr)
            curr.pop()
            dfs(num + 1, curr)
            return
            
        
        dfs(1, [])
        print(lis)
        return lis
        
