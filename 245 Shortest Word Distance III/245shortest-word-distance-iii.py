class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        if word1 == word2:
            fir = {}
            minDist = float('inf')
            for i, word in enumerate(wordsDict):
                if word in fir and word1 == word:
                    minDist = min(minDist, abs(i - fir[word]))
                fir[word] = i
            
            return minDist
                    
                

        hmap = defaultdict(list)

        for i, word in enumerate(wordsDict):
            hmap[word].append(i)
        
        i, j = 0, 0
        lis1 = hmap[word1]
        lis2 = hmap[word2]
        minDist = float('inf')

        while i < len(lis1) and j < len(lis2):
            minDist = min(minDist, abs(lis2[j] - lis1[i]))
            if lis1[i] < lis2[j]:
                i += 1
            elif lis2[j] < lis1[i]:
                j += 1
            else:
                i += 1
                j += 1
        
        return minDist