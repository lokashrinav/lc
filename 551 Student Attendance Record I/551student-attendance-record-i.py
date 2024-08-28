class Solution:
    def checkRecord(self, s: str) -> bool:
        countA = 0
        countL = 0
        maxCountL = 0
        for i in s:
            if i == 'A':
                countA += 1
            if i == 'L' and countL == 0:
                countL += 1
            elif i == 'L' and countL >= 1:
                countL += 1
                maxCountL = max(countL, maxCountL)
            else:
                countL = 0
        maxCountL = max(countL, maxCountL)
        
        if countA < 2 and maxCountL < 3:
            return True
        return False

        