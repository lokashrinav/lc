class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        hmap = {'T': 0, 'F': 0}
        start = 0
        count = 0
        maxCount = 0
        for i in range(len(answerKey)):
            hmap[answerKey[i]] = hmap.get(answerKey[i], 0) + 1
            while min(hmap.values()) > k:
                hmap[answerKey[start]] -= 1
                start += 1
            count = i - start + 1
            maxCount = max(count, maxCount)
        
        return maxCount
        
        

        