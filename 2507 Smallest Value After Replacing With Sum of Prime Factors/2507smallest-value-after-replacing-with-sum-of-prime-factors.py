class Solution:
    def smallestValue(self, n: int) -> int:
        def prime_factors(n):
            factors = []
            divisor = 2
            while n > 1:
                while n % divisor == 0:
                    factors.append(divisor)
                    n //= divisor
                divisor += 1
            return factors
        
        hset = set()
        minSoFar = n
        while len(prime_factors(n)) != 1:
            returned = prime_factors(n)
            n = sum(prime_factors(n))
            minSoFar = min(minSoFar, n)
            if n in hset:
                break
            hset.add(n)
        
        return minSoFar




        