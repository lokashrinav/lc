class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        lis1 = version1.split('.')
        lis2 = version2.split('.')

        for i in range(max(len(lis1), len(lis2))):
            if i >= len(lis1):
                num1 = "0"
                num2 = lis2[i]
            elif i >= len(lis2):
                num2 = "0"
                num1 = lis1[i]
            else:
                num1 = lis1[i]
                num2 = lis2[i]
            
            if int(num1) > int(num2):
                return 1
            elif int(num2) > int(num1):
                return -1
        
        return 0
        
            


        