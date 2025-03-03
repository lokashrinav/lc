class Solution:
    def getFactors(self, n: int) -> List[List[int]]:

        res = []
        def dfs(num, start, path):
            if path:
                res.append(path + [num])

            for i in range(start, int(num ** (1/2)) + 1):
                if num % i == 0:
                    path.append(i)
                    dfs(num // i, i, path)
                    path.pop()
        
        dfs(n, 2, [])
        return res
        


        