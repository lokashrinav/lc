class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, sum(piles)
        saved = float('inf')

        while l <= r:
            m = (l + r) // 2
            total = 0
            for i in range(len(piles)):
                total += math.ceil(piles[i] / m)
            if total > h:
                l = m + 1
            else:
                saved = min(saved, m)
                r = m - 1
        
        return saved
            
