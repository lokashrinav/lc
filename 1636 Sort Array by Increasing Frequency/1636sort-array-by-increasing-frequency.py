class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        hmap = Counter(nums)

        arr = sorted(hmap.items(), key=lambda x: (x[1], -x[0]))

        res = []

        for y, x in arr:
            res += [y] * x
        
        return res
        