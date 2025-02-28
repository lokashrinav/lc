class Solution:
    def grayCode(self, n: int) -> List[int]:
        # 1000
        # 0000

        # 1000 & 0000
        res = [0]
        for i in range(n):
            prefix = 1 << i
            for elem in reversed(res):
                res.append(prefix | elem)
        
        return res
            
