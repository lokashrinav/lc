class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        hmap = Counter(arr)

        maxNum = 0
        saved = 0
        for key, val in hmap.items():
            if val > maxNum:
                saved = key
                maxNum = val

        return saved