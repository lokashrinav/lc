class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:

        res = [1, 1]
        hset = set([1])

        while res[-1] + res[-2] <= k:
            res.append(res[-1] + res[-2])
            hset.add(res[-1] + res[-2])
        
        print(res)

        i = len(res) - 1
        count = 0

        while i >= 0:
            #print(i,  k)

            if k >= res[i]:
                count += 1
                k -= res[i]
            i -= 1
        
        return count
                





        