class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hmap = Counter(s)

        res = []
        for i in range(len(order)):
            if order[i] in hmap:
                res.append(order[i] * hmap[order[i]])
                del hmap[order[i]]
        
        for key in hmap.keys():
            res.append(hmap[key] * key)
        
        return ''.join(res)
        
        
            
        

        