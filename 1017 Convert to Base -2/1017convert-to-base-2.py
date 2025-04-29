class Solution:
    def baseNeg2(self, n: int) -> str:

        '''
        4 -2 0

        2
        -1
        0
        '''
        if n == 0:
            return "0"
            
        res = []
        while n:
            rem = abs(n) % 2
            res.append(rem)
            n = ceil(n / -2)
        
        return ''.join(str(s) for s in res[::-1])
        

        