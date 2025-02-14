class Solution:
    def numberCount(self, a: int, b: int) -> int:

        def isUnique(num):
            str1 = str(num)
            hset = set()
            for i in range(len(str1)):
                if str1[i] in hset:
                    return 0
                else:
                    hset.add(str1[i])
                    
            return 1


        count = 0
        for i in range(a, b + 1):
            count += isUnique(i)

        return count        