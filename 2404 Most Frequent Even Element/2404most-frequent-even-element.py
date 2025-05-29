class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:

        hmap = Counter(nums)

        fun = -1
        saved = 0

        for key, val in hmap.items():
            if key % 2 == 0 and val > hmap[fun]:
                fun = key
            elif key % 2 == 0 and val == hmap[fun]:
                fun = min(key, fun)
        
        return fun
        