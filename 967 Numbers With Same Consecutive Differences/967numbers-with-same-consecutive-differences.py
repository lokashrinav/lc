class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:

        res = set()
        def dfs(num, leng):
            print(num, leng)
            if leng == n:
                res.add(num)
                return
            
            last = num % 10

            if last - k >= 0:
                dfs(num * 10 + (last - k), leng + 1)   
            
            if last + k <= 9:
                dfs(num * 10 + (last + k), leng + 1)

        for i in range(1, 10):
            dfs(i, 1)
        
        return list(res)

        