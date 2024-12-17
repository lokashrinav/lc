class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        operators = {'+', '-', '*'}

        def operator(num1, num2, operation):
            if operation == '+':
                return num1 + num2
            elif operation == '-':
                return num1 - num2
            else:
                return num1 * num2

        def backtrack(left, right):
            res = []

            for i in range(left, right+1):
                if expression[i] in operators:
                    lis1 = backtrack(left, i - 1)
                    lis2 = backtrack(i + 1, right)

                    for f in lis1:
                        for a in lis2:
                            res.append(operator(f, a, expression[i]))

            if res == []:
                res.append(int(expression[left:right+1]))

            return res
        

        return backtrack(0, len(expression) - 1)

        