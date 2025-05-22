class Solution:
    def findDerangement(self, n: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2

        p1, p2 = 1, 2

        '''

        1 -> 0

        2 -> 1

        3 -> 2

        4 -> 9

        5 -> 44

        '''

        for i in range(3, n):
            new = p1 + p2
            p1 = p2
            p2 = new * i % (10 ** 9 + 7)
        
        return p2 % (10 ** 9 + 7)


        

        '''

        1

        1 + 1

        3 + 3 + 3

        11 + 11 + 11 + 11



        1, 2, 3

        3, 1, 2

        2, 3, 1

        ---

        1, 2, 3, 4 

        4, 1, 2, 3

        4, 3, 1, 2

        4, 3, 2, 1

        2, 1, 4, 3

        2, 3, 4, 1

        2, 4, 1, 3

        3, 1, 4, 2

        3, 4, 2, 1

        3, 4, 1, 2



        '''
        
        return 