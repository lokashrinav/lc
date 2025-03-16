class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l, r = 0, max(ranks) * cars * cars
        minutes = float('inf')

        while l <= r:
            m = (l + r) // 2
            res = 0
            for i in range(len(ranks)):
                res += int(math.sqrt(m / ranks[i]))

            if res >= cars:
                minutes = min(m, minutes)
                r = m - 1
            else:
                l = m + 1
    
        return minutes
