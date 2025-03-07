class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        prime = [True] * (right + 1)
        prime[0:2] = [False, False]

        for i in range(2, int(right ** 1/2) + 1):
            if prime[i]:
                for p in range(i * i, right + 1, i):
                    prime[p] = False
        
        primes = [i for i in range(left, right + 1) if prime[i]]

        if len(primes) < 2:
            return [-1, -1]

        curr = [-1, -1]
        minDiff = float('inf')
        for i in range(len(primes) - 1):
            if primes[i + 1] - primes[i] < minDiff:
                minDiff = primes[i + 1] - primes[i]
                curr = [primes[i], primes[i + 1]]
        
        return curr

