class Solution:
    def findNthDigit(self, n: int) -> int:
        '''

        bin search

        452
        100
        
        '''

        def countDig(num2):
            og = len(str(num2))
            total = 0
            while num2 > 0:
                curr = 10 ** (og - 1)
                total += og * (num2 - curr + 1)
                og -= 1
                num2 = curr - 1
            
            return total
        
        #print(countDig(9))


        l, r = 0, n

        while l < r:
            m = (l + r) // 2
            # print(m, countDig(m))
            if countDig(m) >= n:
                r = m
            else:
                l = m + 1
                        
        count1 = countDig(l - 1)

        n -= count1

        #print(n, str(l))

        return int(str(l)[n - 1])

        