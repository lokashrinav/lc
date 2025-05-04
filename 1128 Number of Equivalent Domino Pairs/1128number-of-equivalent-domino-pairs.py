class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        
        hmap = {}
        total = 0

        for y, x in dominoes:
            if (y, x) in hmap:
                total += hmap[(y, x)]
                hmap[(y, x)] += 1
            elif (x, y) in hmap:
                total += hmap[(x, y)]
                hmap[(x, y)] += 1
            else:
                hmap[(y, x)] = 1
        
        return total
            