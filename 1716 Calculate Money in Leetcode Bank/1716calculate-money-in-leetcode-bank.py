class Solution:
    def totalMoney(self, n: int) -> int:
        # 7 * (7 + 1) // 2
        # 8 * (8 + 1) // 2

        rem = n % 7
        calc = n // 7
        sum1 = 0

        print(rem, calc)

        for i in range(calc):
            sum1 += (7 + i) * (8 + i) // 2
            print('1', sum1)
            sum1 -= (i) * (i + 1) // 2
            print('2', sum1)
        
        sum1 += (rem + calc) * (rem + 1 + calc) // 2
        sum1 -= (calc) * (calc + 1) // 2

        print('3', sum1)

        return sum1

        '''

        1 + 2 + 3 + 4 + 5 + 6 + 7 = 28
        
        2 + 3 + 4 + 5 + 6 + 7 + 8

        '''
        