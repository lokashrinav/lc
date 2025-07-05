class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hmap = Counter(arr)
        res = []
        for elem in arr:
            if elem == hmap[elem]:
                res.append(elem)

        return max(res) if res else -1
        