class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        res = []
        for word in words:
            smallest = None
            count = None
            for p in range(len(word)):
                if smallest is None:
                    smallest = word[p]
                    count = 1
                else:
                    if ord(word[p]) < ord(smallest):
                        smallest = word[p]
                        count = 1
                    elif word[p] == smallest:
                        count += 1
                    
            res.append(count)

        res2 = []
        for word in queries:
            smallest = None
            count = None
            for p in range(len(word)):
                if smallest is None:
                    smallest = word[p]
                    count = 1
                else:
                    if ord(word[p]) < ord(smallest):
                        smallest = word[p]
                        count = 1
                    elif word[p] == smallest:
                        count += 1
                    
            res2.append(count)
        
        res.sort()
        final = []

        for elem in res2:
            l, r = 0, len(res) - 1
            ind = bisect_left(res, elem + 1)
            final.append(len(res) - ind)
        
        return final
        

        
        
