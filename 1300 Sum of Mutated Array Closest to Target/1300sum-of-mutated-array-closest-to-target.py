class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:

        if sum(arr) <= target:
            return max(arr)

        close = None
        saved = None

        l, r = 0, target

        while l <= r:
            m = (l + r) // 2
            prev = arr[::]

            for i in range(len(arr)):
                if arr[i] >= m:
                    prev[i] = m
            
            if close is None:
                close = sum(prev)
                saved = m
            elif abs(close - target) > abs(sum(prev) - target):
                close = sum(prev)
                saved = m
            elif abs(close - target) == abs(sum(prev) - target) and m < saved:
                close = sum(prev)
                saved = m

            if sum(prev) > target:
                r = m - 1
            else:
                l = m + 1

        return saved                
                



