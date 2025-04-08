class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        hmap = Counter(words)

        arr = [None] * (len(words) + 1)

        for key, val in hmap.items():
            if arr[val] is None:
                arr[val] = []
            arr[val].append(key)
        
        for elem in arr:
            if elem:
                elem.sort()
        
        res = []
        ind = len(arr) - 1
        while k:
            while not arr[ind]:
                ind -= 1

            for i in range(len(arr[ind])):
                res.append(arr[ind][i])
                k -= 1
                if k == 0:
                    return res
            ind -= 1
        
        return res