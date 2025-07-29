class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:

        '''
        7 = 4, 3
        '''

        total = 0
        for i in range(1, n+1):
            
            calc = n / i + (i - 1) / 2
            #print(calc)
            
            if calc < i:
                return total

            #print(calc)

            if calc % 1 == 0:
                total += 1

        return total
        