class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:

        hmap = defaultdict(int)

        for word in words:
            res1, res2 = defaultdict(int), defaultdict(int)
            for i in range(len(word)):
                if i % 2 == 0:
                    res1[word[i]] += 1
                else:
                    res2[word[i]] += 1
            
            hmap[(frozenset(res1.items()), frozenset(res2.items()))] += 1
                
        return len(hmap.keys())
        

        