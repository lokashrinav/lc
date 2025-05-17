class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        hmap = {}
        minNum = 0
        for i in range(len(list1)):
            hmap[list1[i]] = i
        
        res = []
        curr = float('inf')
        
        for i in range(len(list2)):
            if list2[i] in hmap:
                if hmap[list2[i]] + i < curr:
                    res = [list2[i]]
                    curr = hmap[list2[i]] + i
                elif hmap[list2[i]] + i == curr:
                    res.append(list2[i])
        
        return res

        