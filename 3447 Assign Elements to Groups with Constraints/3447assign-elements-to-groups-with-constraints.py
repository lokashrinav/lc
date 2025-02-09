class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:

        hmap = {}
        res = []
        for i in range(len(elements)):
            if elements[i] not in hmap:
                hmap[elements[i]] = i

        hmap2 = {}
        for i in range(len(groups)):
            if groups[i] in hmap2:
                res.append(hmap2[groups[i]])
                continue
                
            hmap2[groups[i]] = float('inf')
            
            for p in range(1, int(math.sqrt(groups[i])) + 1):
                if groups[i] % p == 0:
                    if p in hmap:
                        hmap2[groups[i]] = min(hmap[p], hmap2[groups[i]])
                    if (groups[i] // p) in hmap:
                        hmap2[groups[i]] = min(hmap[(groups[i] // p)], hmap2[groups[i]])
            if hmap2[groups[i]] == float('inf'):
                hmap2[groups[i]] = -1
            
            res.append(hmap2[groups[i]])
            
        return res
                        
                
            