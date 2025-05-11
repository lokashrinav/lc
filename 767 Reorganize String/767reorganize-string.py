class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = []

        '''
        a b

        a b a a

        a b a

        if odd: max is allowed to be 1 + len(res) // 2
        if even: max is allowed to be 

        '''

        for key, val in count.items():
            if len(s) % 2 == 0 and val > len(s) // 2:
                return ""
            elif len(s) % 2 and val - 1 > len(s) // 2:
                return ""
            
            maxHeap.append((-val, key))
        
        heapify(maxHeap)
        res = ""

        while maxHeap:
            out1, val1 = heappop(maxHeap)
            if maxHeap:
                out2, val2 = heappop(maxHeap)
            else:
                out2 = -1
                val2 = ""

            res += (val1 + val2)

            if out1 + 1 < 0:
                heappush(maxHeap, (out1 + 1, val1))
            if out2 + 1 < 0:
                heappush(maxHeap, (out2 + 1, val2))
        
        return res

        

        
