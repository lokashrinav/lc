class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        while n != 1:
            count = 0
            for i in range(3):
                if n % 5 == 0:
                    n = n / 5
                    count += 1
                elif n % 3 == 0:
                    n = n / 3
                    count += 1
                elif n % 2 == 0:
                    n = n / 2
                    count += 1
            if count == 0:
                return False
        
        return True
        