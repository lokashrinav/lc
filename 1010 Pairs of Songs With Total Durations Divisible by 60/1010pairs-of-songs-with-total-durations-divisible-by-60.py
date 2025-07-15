class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        hmap = defaultdict(int)
        total = 0
        
        for i in range(len(time)):
            if time[i] % 60 == 0:
                total += hmap[0]
            else:
                total += hmap[60 - time[i] % 60]
            hmap[time[i] % 60] += 1
        
        return total

        