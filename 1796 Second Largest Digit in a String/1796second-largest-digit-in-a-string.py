class Solution:
    def secondHighest(self, s: str) -> int:

        maxNum = -1
        maxNum2 = -1
        for elem in s:
            if elem.isdigit():
                if int(elem) == maxNum or int(elem) == maxNum2:
                    continue
                if int(elem) > maxNum:
                    maxNum2 = maxNum
                    maxNum = int(elem)
                elif int(elem) > maxNum2:
                    maxNum2 = int(elem)
        
        return maxNum2
        