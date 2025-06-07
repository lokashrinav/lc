class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        '''

        0, 12, 24

        '''

        hmap = defaultdict(int)
        for elem in hours:
            hmap[elem % 24] += 1
        
        print(hmap)
        
        total = 0
        for key, val in list(hmap.items()):
            if key == 12:
                total += val * (val - 1) // 2
                    # 2 -> 1, 4 -> 
                    # 3 -> 3, 1 -> 0, 5 -> 
            elif key == 0:
                total += val * (val - 1) // 2
            else:
                total += val * hmap[24 - key] / 2
        
        return int(total)

        