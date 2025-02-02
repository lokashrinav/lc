class Solution:
    def isHappy(self, n: int) -> bool:
        def change(num):
            sum1 = 0
            while num:
                rem = num % 10
                num //= 10
                sum1 += rem * rem
            return sum1

        v = n
        n = change(n)
        print(n, v)
        while n != 1 and change(n) != 1:
            if n == 0:
                return False
            if n == v:
                return False
            n = change(change(n))
            v = change(v)
            print(n, v)

        return True
        