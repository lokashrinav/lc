class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        hmap = Counter(arr)
        
        count = 0

        for elem in arr:
            if hmap[elem] == 1:
                count += 1
            if count == k:
                return elem
        
        return ""

        