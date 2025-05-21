class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        '''
        
        1010
        0111

        1101

        '''

        end = start ^ goal
        count = 0

        while end:
            count += end & 1
            end = end >> 1
        
        return count

        