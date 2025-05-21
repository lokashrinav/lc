class Solution:
    def encode(self, num: int) -> str:

        '''
        1
        10
        11
        100
        101
        110
        111
        1000
        '''

        num += 1

        res = []
        
        x = (num)

        while x:
            res.append(x & 1)
            x = x >> 1
        
        res.pop()

        res.reverse()

        return ''.join(str(s) for s in res)