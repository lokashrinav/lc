class Solution:
    def reorganizeString(self, s: str) -> str:
        hmap = Counter(s)
        maxHeap = [(-x, y) for y, x in hmap.items()]
        heapify(maxHeap)

        res = []
        while maxHeap:
            if res and len(maxHeap) == 1 and maxHeap[0] == res[-1]:
                return ""
            if len(maxHeap) == 1:
                x, y = heappop(maxHeap)
                res.append(y)
                if x != -1:
                    return ""
                break                                        

            x1, y1 = heappop(maxHeap)
            x2, y2 = heappop(maxHeap)

            res.append(y1)
            res.append(y2)

            if x1 != -1:
                heappush(maxHeap, (x1 + 1, y1))
            if x2 != -1:
                heappush(maxHeap, (x2 + 1, y2))
        
        for i in range(1, len(res)):
            if res[i] == res[i - 1]:
                return ""
        
        return ''.join(res)