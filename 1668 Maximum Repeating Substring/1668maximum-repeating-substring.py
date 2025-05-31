class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:

        l, r = 0, len(sequence)

        maxNum = 0

        while l <= r:
            m = (l + r) // 2
            word2 = ""
            for i in range(m):
                word2 += word
            
            if word2 in sequence:
                l = m + 1
                maxNum = max(maxNum, m)
            else:
                r = m - 1
        
        return maxNum

        