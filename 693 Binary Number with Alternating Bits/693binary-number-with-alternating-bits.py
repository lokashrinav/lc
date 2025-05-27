class Solution:
    def hasAlternatingBits(self, n: int) -> bool:

        '''

        2 4 8 16 32

        '''

        '''

        111

        '''

        saved1 = saved2 = None
        count = 0

        while n:
            a = n & 1
            if count == 0:
                saved1 = a
            elif count == 1:
                if a == saved1:
                    return False

                saved2 = a
            elif count % 2 == 0 and saved1 != a:
                return False
            elif count % 2 and saved2 != a:
                return False

            count += 1
            n = n >> 1
        
        return True
        