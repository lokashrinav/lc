class Solution:
    def twoEggDrop(self, n: int) -> int:
        '''

        15 = 5
        14 -> Drop = 5
        13
        12 -> Drop = 5
        11
        10
        9 -> Drop = 5
        8
        7 
        6
        5 -> Drop = 5
        4 
        3
        2
        1

        10 -> 1 + 2 + 3

        ((n + 1) * n) >= 20

        n ** 2 + n - 20 >= 0

        (n + 5)(n - 4) >= 0
        
        '''

        count = 0
        first = 1
        for i in range(n):
            if count == first:
                first += 1
                count = 0
            count += 1
        
        return first

        