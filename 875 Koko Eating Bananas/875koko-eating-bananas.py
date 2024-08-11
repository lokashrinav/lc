class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calculate(piles, k):
            count = 0
            for i in piles:
                count += math.ceil(i / k)
            return count

        l = 1
        r = max(piles)

        minHours = float('inf')
        while l <= r:
            m = (l + r) // 2
            hours = calculate(piles, m)
            print(m, hours)
            if hours <= h:
                minHours = min(minHours, m)
                r = m - 1
            elif hours > h:
                l = m + 1
        if minHours == float('inf'):
            return 0  
        return minHours


        