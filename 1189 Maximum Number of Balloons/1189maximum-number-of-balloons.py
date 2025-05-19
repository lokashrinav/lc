class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hmap = Counter(text)

        minNum = float('inf')

        for s in "balon":
            if s == "l" or s == "o":
                minNum = min(minNum, hmap[s] // 2)
            else:
                minNum = min(minNum, hmap[s])

        return minNum if minNum != float('inf') else 0
