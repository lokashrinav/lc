class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        hmap = Counter(arr1)
        res = []
        hset = set(arr2)
        for i in range(len(arr2)):
            if arr2[i] in hmap:
                res += [arr2[i]] * hmap[arr2[i]]
        
        next1 = []
        for i in range(len(arr1)):
            if arr1[i] not in hset:
                next1.append(arr1[i])
        next1.sort()

        res += next1

        
        return res