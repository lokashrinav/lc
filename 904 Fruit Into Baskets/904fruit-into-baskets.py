class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count1, count2 = 0, 0
        num1, num2 = None, None
        start = 0
        maxDist = 0
        for i in range(len(fruits)):
            if num1 is None:
                num1 = fruits[i]
                count1 = 1
            elif fruits[i] == num1:
                count1 += 1
            elif num2 is None:
                num2 = fruits[i]
                count2 = 1
            elif fruits[i] == num2:
                count2 += 1
            else:
                while count1 and count2:
                    if fruits[start] == num1:
                        count1 -= 1
                    elif fruits[start] == num2:
                        count2 -= 1
                    start += 1
                if count1 == 0:
                    num1 = fruits[i]
                    count1 = 1
                elif count2 == 0:
                    num2 = fruits[i]
                    count2 = 1
            maxDist = max(maxDist, i - start + 1)
        print(i, start)
        return maxDist



