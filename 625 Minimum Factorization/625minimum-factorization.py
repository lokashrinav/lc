class Solution:
    def smallestFactorization(self, num: int) -> int:
        
        if len(str(num)) == 1:
            return num
        
        res = []
        while num > 1:
            change = True
            for i in range(9, 1, -1):
                if num % i == 0:
                    num = num // i
                    res.append(i)
                    change = False
                    break

            if change:
                return 0
        
        res.sort()
        num = int(''.join(str(s) for s in res))
        return num if num <= 2 ** 31 - 1 else 0