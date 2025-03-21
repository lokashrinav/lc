class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        res = []
        def dfs(num):
            res.append(int(num))
            for i in range(0, 10):
                if int(num + str(i)) <= n:
                    dfs(num + str(i))

        for i in range(1, 10):
            if int(i) <= n:
                dfs(str(i))

        return res

