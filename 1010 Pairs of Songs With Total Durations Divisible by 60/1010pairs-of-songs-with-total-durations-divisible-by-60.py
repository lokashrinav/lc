class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        hmap = defaultdict(int)
        total = 0
        hmap[60] = 1
        for i in range(len(time)):
            curr = time[i] % 60
            if curr in hmap:
                total += hmap[curr]
            hmap[(60 - curr) % 60] += 1
        
        return total

        