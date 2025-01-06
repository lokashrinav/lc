class Solution:
    def solveEquation(self, equation: str) -> str:
        i = 0
        prevEq = None
        count = 0
        total = 0
        while i < len(equation) and equation[i] != '=':
            num = ''
            while i < len(equation) and (equation[i] != '+' and (equation[i] != '-' or i == 0) and equation[i] != '='):
                num += equation[i]
                i += 1     

            if (num[0] == '-') and 'x' in num:
                if len(num) == 2:
                    count -= 1
                else:
                    count -= int(num[1:-1])
            elif prevEq == '-' and 'x' in num:
                if len(num) == 1:
                    count -= 1
                else:
                    count -= int(num[0:-1])
            elif 'x' in num:
                if len(num) == 1:
                    count += 1
                else:
                    count += int(num[0:-1])
            elif num[0] == '-':
                total -= int(num[1:])
            elif prevEq == '-':
                total -= int(num)
            else:
                total += int(num)
                                    
            if equation[i] == '=':
                break
            
            if i != len(equation):
                prevEq = equation[i]
                i += 1

        prevTotal = total
        prevCount = count
        total, count = 0, 0

        i += 1
        prevEq = None
        while i < len(equation):
            num = ''
            while i < len(equation) and (equation[i] != '+' and (equation[i] != '-' or equation[i - 1] == '=')):
                num += equation[i]
                i += 1                
            
            if (num[0] == '-') and 'x' in num:
                if len(num) == 2:
                    count -= 1
                else:
                    count -= int(num[1:-1])
            elif prevEq == '-' and 'x' in num:
                if len(num) == 1:
                    count -= 1
                else:
                    count -= int(num[0:-1])
            elif 'x' in num:
                if len(num) == 1:
                    count += 1
                else:
                    count += int(num[0:-1])
            elif num[0] == '-':
                total -= int(num[1:])
            elif prevEq == '-':
                total -= int(num)
            else:
                total += int(num)
            
            if i != len(equation):
                prevEq = equation[i]
                i += 1        

        print(prevTotal, total)
        print(prevCount, count)

        leftX = prevCount - count
        rightX = total - prevTotal
        print(leftX, rightX)

        if leftX == 0 and rightX == 0:
            return "Infinite solutions"
        elif leftX == 0:
            if total != prevTotal:
                return "No solution"
            else:
                return "Infinite solutions"
        elif rightX == 0:
            return 'x=0'
        else:
            fun = rightX // leftX
            return 'x=' + str(fun)
        
        

        




            




            



                        
            
            

            

        