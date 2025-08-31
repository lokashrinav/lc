class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:

        def other(num):
            res = []
            for i in range(1, int(num ** (1/2)) + 1):
                if num % i == 0:
                        res.append((i, num // i))
            return res
            
        def rec(num, k):
            if k == 1:
                return [num]

            returned = other(num)
            # print(num, k, returned)

            maxing = None
            for first, last in returned:
                if k % 2:
                    val1 = rec(first, k // 2 + 1)
                    val2 = rec(first, k // 2)
                    val3 = rec(last, k // 2 + 1)
                    val4 = rec(last, k // 2)
                    if max(max(val1), max(val4)) -  min(min(val1), min(val4)) < max(max(val2), max(val3)) -  min(min(val2), min(val3)):
                        final = val1 + val4
                    else:
                        final = val2 + val3
                else:
                    val1 = rec(first, k // 2)
                    val2 = rec(last, k // 2)
                    final = val1 + val2

                # print(final)
                
                if maxing is None:
                    maxing = final
                else:
                    if max(maxing) -  min(maxing) > max(final) - min(final):
                        maxing = final

            return maxing
                       
        return rec(n, k)

        '''

        2, 5, 2, 5

        2, 2, 11
        
        '''


        '''res = []
        i = 2
        while n != 1:
            if n % i == 0:
                res.append(i)
                n //= i
            else:
                i += 1

        print(res)
        while len(res) > k:
            out = heappop(res)
            out2 = heappop(res)

            heappush(res, out * out2)

        while len(res) < k:
            res.append(1)

        return res'''
            
        
        
        
        