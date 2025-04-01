class Solution:
    def closestFair(self, n: int) -> int:
        
        def fair(n):
            count = 0
            while n:
                rem = n % 10
                n //= 10
                if rem % 2:
                    count += 1
                else:
                    count -= 1

            return count == 0

        while True:
            print(n)
            if len(str(n)) % 2:
                n = 10 ** (len(str(n)))

            if fair(n):
                return n

            n += 1
