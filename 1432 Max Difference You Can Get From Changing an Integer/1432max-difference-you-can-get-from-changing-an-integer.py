class Solution:
    def maxDiff(self, num: int) -> int:
        
        str1 = list(str(num))
        str2 = str1.copy()
        ind = None
        for i in range(len(str1)):
            ind = i
            if str1[i] != '9':
                break
        
        saved = str1[ind]
        for i in range(len(str1)):
            if str1[i] == saved:
                str1[i] = '9'
        
        maxNum = int(''.join(str1))

        ind = None
        for i in range(len(str2)):
            ind = i
            if (i == 0 and str2[i] != '1') or (i != 0 and str2[i] != '0'):
                if (i != 0 and str2[i] == '1' and str2[0] == '1'):
                    continue
                break
        
        saved = str2[ind]
        for i in range(len(str1)):
            if (ind == 0 and str2[i] == saved) or (saved == '1' and str2[0] == '1'):
                str2[i] = '1'
            elif str2[i] == saved:
                str2[i] = '0'
        
        minNum = int(''.join(str2))

        print(maxNum, minNum)
        return maxNum - minNum

        