class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.idk = defaultdict(list)
        for i in range(len(wordsDict)):
            self.idk[wordsDict[i]].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        i, j = 0, 0
        lis1 = self.idk[word1]
        lis2 = self.idk[word2]
        minDist = float('inf')
        while i < len(lis1) and j < len(lis2):
            minDist = min(minDist, abs(lis2[j] - lis1[i]))
            if lis1[i] < lis2[j]:
                i += 1
            elif lis1[i] > lis2[j]:
                j += 1
            else:
                i += 1
                j += 1

        return minDist
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)