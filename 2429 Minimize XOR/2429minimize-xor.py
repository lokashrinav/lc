class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # 0001
        # 0001 = 0

        '''

        We take the min number of set bits

        remove the top set bits from num1

        '''

        def countBits(x):
            count = 0
            while x:
                count += (x & 1)
                x = x >> 1           
            return count

        count1, count2 = countBits(num1), countBits(num2)

        x = num1

        i = 0
        while count1 > count2:
            if x & (1 << i):
                count1 -= 1
                x = x ^ (1 << i)
            i += 1

        while count2 > count1:
            if x & (1 << i) == 0:
                count2 -= 1
                x = x | (1 << i)
            i += 1

        return x

