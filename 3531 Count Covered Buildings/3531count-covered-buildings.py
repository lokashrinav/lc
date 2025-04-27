class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:

        hset = set((i, j) for i, j in buildings)

        hmap = defaultdict(list)
        
        for x, y in buildings:
            hmap[x].append(y)

        for elem in hmap:
            if (elem, min(hmap[elem])) in hset:
                hset.remove((elem, min(hmap[elem])))
                
            if (elem, max(hmap[elem])) in hset:
                hset.remove((elem, max(hmap[elem])))

        hmap = defaultdict(list)
        for x, y in buildings:
            hmap[y].append(x)

        for elem in hmap:
            if (min(hmap[elem]), elem) in hset:
                hset.remove((min(hmap[elem]), elem))
                
            if (max(hmap[elem]), elem) in hset:
                hset.remove((max(hmap[elem]), elem))

        return len(hset)
        