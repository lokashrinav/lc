class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        hmap = {}
        for ide, score in items:
            if ide not in hmap:
                hmap[ide] = [0, 0, 0, 0, 0]
            first, second, third, fourth, fifth = hmap[ide]
            if score > first:
                hmap[ide][4] = fourth
                hmap[ide][3] = third
                hmap[ide][2] = second
                hmap[ide][1] = first
                hmap[ide][0] = score
            elif score > second:
                hmap[ide][4] = fourth
                hmap[ide][3] = third
                hmap[ide][2] = second
                hmap[ide][1] = score
            elif score > third:
                hmap[ide][4] = fourth
                hmap[ide][3] = third
                hmap[ide][2] = score
            elif score > fourth:
                hmap[ide][4] = fourth
                hmap[ide][3] = score
            elif score > fifth:
                hmap[ide][4] = score
        
        arr = []
        for key in sorted(hmap.keys()):
            arr.append([key, sum(hmap[key]) // 5])
        
        return arr

