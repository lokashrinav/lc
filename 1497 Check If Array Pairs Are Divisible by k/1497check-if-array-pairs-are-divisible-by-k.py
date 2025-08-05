class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        hmap = defaultdict(int)

        for elem in arr:
            hmap[elem % k] += 1

        print(hmap)
        for elem in hmap:
            if (k - elem) % k == elem:
                if hmap[elem] % 2 != 0:
                    return False
                    
            if hmap[(k - elem) % k] != hmap[elem]:
                return False
        
        return True
