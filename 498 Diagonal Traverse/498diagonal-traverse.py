class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        hmap = defaultdict(list)

        for i in range(len(mat)):
            for p in range(len(mat[0])):
                hmap[i + p].append(mat[i][p])
        
        res = []

        for i, key in enumerate(sorted(hmap.keys())):
            if i % 2 == 1:
                for p in range(len(hmap[key])):
                    res.append(hmap[key][p])
            else:
                for p in range(len(hmap[key]) - 1, -1, -1):
                    res.append(hmap[key][p])
        
        return res
