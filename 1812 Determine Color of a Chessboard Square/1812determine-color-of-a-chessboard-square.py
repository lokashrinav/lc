class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:

        '''



        '''

        if int(coordinates[1]) % 2 == 0:
            return ord(coordinates[0]) % 2 == 1
        
        return ord(coordinates[0]) % 2 != 1
        