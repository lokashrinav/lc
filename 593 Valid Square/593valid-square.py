class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        
        pList = [p1, p2, p3, p4]
        pSet = set(map(tuple, pList))
        if len(pSet) <= 3: return False
        hmap = {}

        for i in range(4):
            for j in range(i + 1, 4):
                distance = (pList[i][0] - pList[j][0]) ** 2 + (pList[i][1] - pList[j][1]) ** 2
                hmap[distance] = hmap.get(distance, 0) + 1
        
        if len(hmap) == 2:
            for item, val in hmap.items():
                if val == 4 or val == 2:
                    continue
                else:
                    return False
            return True

        return False


