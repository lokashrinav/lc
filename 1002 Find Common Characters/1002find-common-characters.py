class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        prev = Counter(words[0])

        for i in range(1, len(words)):
            hmap2 = Counter(words[i])

            for elem in list(prev.keys()):
                if elem not in hmap2:
                    if elem in prev:
                        del prev[elem]
                else:
                    prev[elem] = min(prev[elem], hmap2[elem])
        
        res = []
        for key, val in prev.items():
            res += [key] * val
        
        return res

                
        