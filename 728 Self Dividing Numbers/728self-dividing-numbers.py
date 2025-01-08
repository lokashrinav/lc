class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        def checkInclusive(num):
            num2 = str(num)
            for i in range(len(num2)):
                if num2[i] == '0':
                    return False
                elif num % int(num2[i]) != 0:
                    return False
            return True


        for i in range(left, right + 1):
            if checkInclusive(i):
                res.append(i)
        
        return res