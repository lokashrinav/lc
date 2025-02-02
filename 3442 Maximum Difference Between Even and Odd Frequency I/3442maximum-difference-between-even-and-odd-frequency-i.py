class Solution:
    def maxDifference(self, s: str) -> int:
        minEven = float('inf')
        maxOdd = float('-inf')
        hmap = Counter(s)

        for key in hmap.keys():
            if hmap[key] % 2 == 0:
                minEven = min(minEven, hmap[key])
            else:
                maxOdd = max(maxOdd, hmap[key])

        return maxOdd - minEven

        