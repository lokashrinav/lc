class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:

        def func(num):
            total = 0
            for s in str(num):
                total += int(s)
            return total

        hmap = defaultdict(int)

        for i in range(lowLimit, highLimit + 1):
            hmap[func(i)] += 1
        
        return max(hmap.values())
        