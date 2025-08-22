class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        hmap = Counter(arr)

        list1 = list(hmap.items())
        list1.sort(key = lambda x: (x[1], x[0]))
        total = 0
        for i in range(len(list1)):
            key, val = list1[i]
            if val <= k:
                k -= val
                total += 1
            else:
                return len(list1) - total
        
        return 0

