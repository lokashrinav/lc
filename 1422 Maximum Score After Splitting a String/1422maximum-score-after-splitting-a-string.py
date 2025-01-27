class Solution:
    def maxScore(self, s: str) -> int:

        count = 0
        total = s.count('1')

        score = 0
        for i in range(len(s) - 1):
            if s[i] == '0':
                count += 1
            else:
                total -= 1

            score = max(count + total, score)
    
        return score


        