class Solution:
    def maxProduct(self, n: int) -> int:
        str1 = str(n)

        maxNum = 0
        maxInd = None
        for i in range(len(str1)):
            if int(str1[i]) >= maxNum:
                maxNum = int(str1[i])
                maxInd = i

        maxNum2 = 0
        for i in range(len(str1)):
            if int(str1[i]) >= maxNum2 and i != maxInd:
                maxNum2 = int(str1[i])

        return maxNum * maxNum2
            