class Solution:
    def bulbSwitch(self, n: int) -> int:
        '''
        3 -> 2 - round(3 / 2)
        2 -> 1

        71 -> 

        1 0 1 0
        
        '''

        if n == 0:
            return 0
        return int(sqrt(n))
        


        