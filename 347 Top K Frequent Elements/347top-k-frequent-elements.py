class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hmap = Counter(nums)

        arr = [[] for i in range(max(hmap.values()) + 1)]

        for key, val in hmap.items():
            arr[val].append(key)
        
        res = []
        ind = 0
        i = len(arr) - 1
        while i >= 0:
            for p in range(len(arr[i])):
                res.append(arr[i][p])
                if len(res) == k:
                    return res
            i -= 1
        
        return res


        
