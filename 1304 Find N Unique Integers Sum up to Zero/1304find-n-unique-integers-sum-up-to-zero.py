class Solution:
    def sumZero(self, n: int) -> List[int]:

        k = -((n - 1) * n) // 2

        res = [i for i in range(1, n)]

        res.append(k)
        
        return res
        