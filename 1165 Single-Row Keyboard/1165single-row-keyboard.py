class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:

        hmap = {}
        for i in range(len(keyboard)):
            hmap[keyboard[i]] = i
        
        prev = 0
        total = 0
        for s in word:
            total += abs(hmap[s] - prev)
            prev = hmap[s]
        
        return total
        