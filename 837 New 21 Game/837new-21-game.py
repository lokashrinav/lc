class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or k + maxPts <= n:
            return 1.0
        cache = {}
        windowSum = 0
        for i in range(k, k + maxPts):
            windowSum += 1 if i <= n else 0
        
        for i in range(k - 1, -1, -1):
            cache[i] = windowSum / maxPts
            remove = 0
            if i + maxPts <= n:
                remove = cache.get(i + maxPts, 1)
            windowSum += cache[i] - remove
        return cache[0]

    

        