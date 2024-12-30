class Solution:

    def primePalindrome(self, n: int) -> int:
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(sqrt(num)) + 1):
                if num % i == 0:
                    return False
            return True
        
        if n <= 2:
            return 2
        elif n == 3:
            return 3
        elif n <= 5:
            return 5
        elif n <= 7:
            return 7
        elif n <= 11:
            return 11

        for i in range(1, 16):
            for half in range(10**((i - 1) // 2), 10**((i + 1) // 2)):
                h = str(half)
                pali = int(h + h[-2::-1])
                if pali >= n and is_prime(pali):
                    return pali

        