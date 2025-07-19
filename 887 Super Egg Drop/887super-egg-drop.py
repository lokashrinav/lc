import math

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        def floors(x):
            total = 0
            c = 1
            for i in range(1, k + 1):
                c *= x - i + 1
                c //= i
                total += c
                if total >= n:
                    break
            return total

        # Binary search for minimal x such that sum of binomials ≥ n
        low, high = 1, n
        while low < high:
            mid = (low + high) // 2
            if floors(mid) >= n:
                high = mid
            else:
                low = mid + 1
        return low
