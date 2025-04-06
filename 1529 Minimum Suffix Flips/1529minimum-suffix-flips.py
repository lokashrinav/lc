class Solution:
    def minFlips(self, target: str) -> int:
        '''
        00000
        11111
        10000
        10111

        000
        111
        100
        101
        '''

        num = int(target, 2)
        count = 0
        for i in range(len(target) - 1, -1, -1):
            if ((num >> i) & 1):
                num = num ^ ((1 << i) - 1)
                count += 1
        
        return count
        