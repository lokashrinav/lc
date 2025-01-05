class Solution:
    def smallestNumber(self, num: int) -> int:

        if num > 0:
            lis = list(str(num))
            i = 0
            minNum = float('inf')
            while i < len(lis):
                if int(lis[i]) < minNum and int(lis[i]) != 0:
                    minNum = int(lis[i])
                i += 1
            str1 = str(minNum)
            sparrow = True
            lis = sorted(lis)
            for i in range(len(lis)):
                if lis[i] == str(minNum) and sparrow:
                    sparrow = False
                else:
                    str1 += lis[i]
            return int(str1)
        elif num == 0:
            return num
        else:
            lis = list(str(abs(num)))
            return int('-' + ''.join(sorted(lis, reverse=True)))

        