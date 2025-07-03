class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        def die(num):
            res = set()
            for i in range(1, int(num ** (1/2) + 1)):
                if num % i == 0:
                    res.add(i)
                    res.add(num // i)
            
            #print(res)
            return res


        total = 0
        for elem in nums:
            arr = die(elem)
            if len(arr) == 4:
                total += sum(arr)
        
        return total
        