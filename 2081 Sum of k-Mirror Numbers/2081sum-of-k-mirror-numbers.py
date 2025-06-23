class Solution:
    def kMirror(self, k: int, n: int) -> int:

        def check1(lis):
            #if lis[0] == 0:
             #   return False

            return lis == lis[::-1]

        def check2(num):
            str1 = str(num)
            return str1 == str1[::-1]
        
        def con(num):
            res = []
            while num:
                rem = num % k
                num = num // k
                res.append(rem)
            
            return res

        total = 0

        for i in range(1, 10):
            if n == 0:
                break

            if check1(con(i)) and check2(i):
                n -= 1
                total += i
                #print(i)

        num = 1

        first = True

        while n:
            for i in range(num, num * 10):
                if n == 0:
                    break

                curr = int(str(i) + str(i)[::-1])
                #print(curr)

                if check1(con(curr)) and check2(curr):
                    total += curr
                   # print(curr)
                    n -= 1

            for p in range(num, num * 10):
                for i in range(0, 10):
                    if n == 0:
                        break

                    curr = int(str(p) + str(i) + str(p)[::-1])
                   # print(curr)
                    if check1(con(curr)) and check2(curr):
                        total += curr
                        print(curr)
                        n -= 1

            first = False
            num *= 10
        
        return total